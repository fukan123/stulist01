#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

from dbconn import db_cursor

def create_db():
    sqlstr = """
    DROP TABLE IF EXISTS course;

    CREATE TABLE IF NOT EXISTS course  (
        cou_sn   INTEGER,     --序号
        cou_no   TEXT,        --学号
        name     TEXT,        --姓名
        classroom    TEXT,     --班级
        sex     TEXT,        --性别
        birthday TEXT,        --出生日期
        PRIMARY KEY(cou_sn)
    );
    -- CREATE UNIQUE INDEX idx_course_no ON course(cou_no);

    CREATE SEQUENCE seq_cou_sn 
        START 10000 INCREMENT 1 OWNED BY course.cou_sn;

    """
    with db_cursor() as cur :
        cur.execute(sqlstr) # 执行SQL语句
    
def init_data():
    sqlstr = """
    DELETE FROM course;

    INSERT INTO course (cou_sn, cou_no, name,classroom,sex,birthday)  VALUES 
        (101, '1310650307',  '傅勘',  '信息1303',  '男','1994-04-18'), 
        (102, '1310650308',  '伍启保', '信息1303', '男','1995-02-18'),
        (103, '1310650321',  '马晓雅', '信息1303', '女','1994-12-21'),
        (104, '1310650408',  '陈淑芳', '信息1304', '女','1994-04-06'),
        (105, '1310650112',  '寇延婷', '信息1304', '女','1994-12-20'),
        (106, '1310650112',  '寇延婷', '信息1304', '女','1994-12-20');

    """
    with db_cursor() as cur :
        cur.execute(sqlstr)    

if __name__ == '__main__':
    create_db()
    init_data()
    print('数据库已初始化完毕！')
