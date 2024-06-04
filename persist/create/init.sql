create table user (
    id	varchar(30) 				                                        comment '회원 ID'
		primary key,
    password    varchar(255)                                    not null 	comment '비밀번호',
    phone       varchar(255)                                    not null    comment '핸드폰 번호',
    created_at  datetime(6)     default current_timestamp(6)    not null    comment '회원 생성 일자'
) ENGINE=INNODB DEFAULT CHARSET=UTF8 COMMENT='회원 테이블';