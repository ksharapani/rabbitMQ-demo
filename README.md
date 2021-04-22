# rabbitMQ-demo

## create database
sqlite3 database.db

## create table
    CREATE TABLE data (
        random_number integer,
        result_1 integer,
        result_2 integer
    );

## RabbitMQ configuration
    create queue called 'test-q'
    create exchange called 'test-e' (use Type as direct)
    goto 'test-q' and create Bindings (use Routing key as 'test')