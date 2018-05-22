from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base  #描述表结构
from sqlalchemy import Column, String, Integer,BigInteger,DATETIME,SmallInteger,Text,func

from sqlalchemy.orm import sessionmaker,relationship  #与mysql建立会话
from sqlalchemy import ForeignKey       #表建立关系


Base = declarative_base()

class employee(Base):
    __tablename__ = 'employee'
    id = Column('id',Integer, primary_key=True,index=True)
    username = Column('username',String(20), nullable=False)
    password = Column('password',String(256), nullable=False)
    realname = Column('realname',String(50), nullable=False)
    picture = Column('picture',String(512), nullable=False)
    openid = Column('openid',String(128))
    session_key = Column('session_key',String(256))
    unionid = Column('unionid',String(128))
    employeefollownum = relationship('employee_follow',backref='employeefollownum',uselist=False)
    employeefollowcompany = relationship('follow_company',backref='employeefollowcompany')
    employeefollowindustry = relationship('follow_industry', backref='employeefollowindustry')
    employeesession = relationship('session', backref='employeesession',uselist=False)


class  employee_follow(Base):
    __tablename__ = 'employee_follow'
    id = Column('id', Integer,ForeignKey('employee.id'),primary_key=True,index=True)
    company_count = Column('company_count', Integer,nullable=False)
    industry_count = Column('industry_count', Integer, nullable=False)

class  company(Base):
    __tablename__ = 'company'
    id = Column('id',BigInteger, primary_key=True,index=True)
    company_name = Column('company_name',String(256), nullable=False)
    short_name = Column('short_name',String(128),nullable=False)
    is_chinaipo = Column('is_chinaipo',SmallInteger,nullable=False)
    url = Column('url',String(128),nullable=False)
    stock_id = Column('stock_id',String(10))
    compayarticle = relationship('company_article', backref='compayarticle')
    companyfollow = relationship('follow_company', backref='companyfollow')
    companyindustry =  relationship('industry_company', backref='companyindustry')

class  company_article(Base):
    __tablename__ = 'company_article'
    company_id =  Column('company_id',BigInteger,ForeignKey('company.id'),primary_key=True,index=True)
    article_id =  Column('article_id',BigInteger,primary_key=True)

class  follow_company(Base):
    __tablename__ = 'follow_company'
    id = Column('id',BigInteger, primary_key=True,index=True)
    employee_id = Column('employee_id',Integer,ForeignKey('employee.id'), nullable=False)
    company_id = Column('company_id',BigInteger,ForeignKey('company.id'), nullable=False)
    follow_time = Column('follow_time',DATETIME, nullable=False)
    is_follow = Column('is_follow',SmallInteger, nullable=False,default=1)
    unfollow_time = Column('unfollow_time',DATETIME)

class  follow_industry(Base):
    __tablename__ = 'follow_industry'
    id = Column('id',BigInteger, primary_key=True,index=True)
    employee_id = Column('employee_id',Integer,ForeignKey('employee.id'),nullable=False)
    industry_id = Column('industry_id',BigInteger,ForeignKey('industry.id'), nullable=False)
    follow_time = Column('follow_time',DATETIME, nullable=False)
    is_follow = Column('is_follow',SmallInteger, nullable=False,default=1)
    unfollow_time = Column('unfollow_time',DATETIME)

class  industry(Base):
    __tablename__ = 'industry'
    id = Column('id',Integer, primary_key=True,index=True)
    industry_name = Column('industry_name',String(128),nullable=False)
    parent_id = Column('parent_id',Integer)
    children_count = Column('children_count',Integer,nullable=False)
    industryfollow = relationship('follow_industry', backref='industryfollow')
    industryarticle = relationship('industry_article', backref='industryarticle')
    industrycompay = relationship('industry_company', backref='industrycompay')


class  industry_article(Base):
    __tablename__ = 'industry_article'
    industry_id = Column('industry_id',Integer,ForeignKey('industry.id'), primary_key=True,index=True)
    article_id = Column('article_id',BigInteger, primary_key=True,index=True)

class  industry_company(Base):
    __tablename__ = 'industry_company'
    industry_id = Column('industry_id',Integer,ForeignKey('industry.id'), primary_key=True,index=True)
    company_id = Column('company_id',BigInteger,ForeignKey('company.id'), primary_key=True,index=True)

class  session(Base):
    __tablename__ = 'session'
    id = Column('id',String(36), primary_key=True,index=True)
    openid = Column('openid',String(128),nullable=False)
    employee_id = Column('employee_id', Integer, ForeignKey('employee.id'))
    create_time = Column('create_time',DATETIME, nullable=False)
    enable = Column('enable',SmallInteger, nullable=False,default=1)
    expire_time = Column('expire_time',DATETIME, nullable=False)
    session_key = Column('session_key',String(256),nullable=False)
    random = Column('random',Integer,nullable=False)

class article(Base):
    __tablename__ = 'article'
    id = Column('id',BigInteger, primary_key=True,index=True)
    title = Column('title',String(256),nullable=False)
    thumb_img = Column('thumb_img',String(256))
    url = Column('url',String(512),nullable=False)
    description = Column('description',Text)
    publish_time = Column('publish_time',DATETIME,nullable=False)
    text = Column('text',Text,nullable=False)
    create_time = Column('create_time',DATETIME,nullable=False)
    source_site = Column('source_site',String(128),nullable=False)
    body = Column('body',Text,nullable=False)

class employee_article(Base):
    __tablename__ = 'employee_article'
    employee_id = Column('employee_id',Integer, primary_key=True,index=True)
    article_id = Column('article_id',BigInteger, primary_key=True,index=True)
    is_read = Column('is_read',SmallInteger,nullable=False)
    is_invalid = Column('is_invalid',SmallInteger,nullable=False)
    is_send = Column('is_send',SmallInteger,nullable=False)
    send_time = Column('send_time',DATETIME)

if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:123456@localhost:3307/yuqing?charset=utf8')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    dbsession = Session()

    aa = dbsession.query(employee).filter(employee.id == 1)


    # dbsession.query.filter(employee.id == 110).update({employee.usernma: 'c'})

    # a = dbsession.query(employee).filter(employee.id == 110).one()#.update({employee.username: 'shenb'}, synchronize_session=False)
    # dbsession.query(employee).filter(employee.id == 110).update({'username':'12345'})
    # a['username']='111'

    # dbsession.commit()
