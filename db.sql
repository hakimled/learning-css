--this  is an sql comment
create TABLE users(
    id int unsigned auto_increment ,
    username varchar(20) not null ,
    age int(3) not null,
    primary key(id)
    key(username)
    
);
insert into users(username) values('hakim');
