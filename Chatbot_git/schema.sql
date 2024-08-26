
create database tests;
use tests;
Create table dim_lab
                            (
                                lab_id varchar(25),
                                lab_name varchar(25)
                            );
                            create table dim_hosp
                            (
                                hosp_id varchar(25),
                                hosp_name varchar(25)
                            );
                            create table dim_test_dept
                            (
                                test_dept_id varchar(25),
                                test_dept_name varchar(25)
                            );
                            create table dim_test
                            (
                                test_id varchar(25),
                                test_name varchar(25),
                                test_dept_id varchar(25)
                            );
                            create table dim_result
                            (
                                result_id varchar(25),
                                test_id varchar(25),
                                result_value varchar(25),
                                result_unit varchar(25),
                                result_range varchar(25),
                                result_status varchar(25)
                            );
                            create table dim_sample
                            (
                                sample_id varchar(25),
                                collect_date date
                            );
                            create table dim_patient
                            (
                                patient_id varchar(25),
                                admit_date date,
                                discharge_date date,
                                hosp_id varchar(25)
                            );
                            create table dim_doctor
                            (
                                doctor_id varchar(25),
                                doctor_name varchar(25)
                            );
                            create table fact_test_result
                            (
                                lab_id varchar(25),
                                hosp_id varchar(25),
                                test_id varchar(25),
                                sample_id varchar(25),
                                patient_id varchar(25),
                                doctor_id varchar(25),
                                request_date date,
                                test_date date,
                                result_date date,
                                result_id varchar(25),
                                is_rerun boolean,
                                is_addon boolean
                            );
                            create table fact_events
                            (
                                lab_id varchar(25),
                                hosp_id varchar(25),
                                test_id varchar(25),
                                sample_id varchar(25),
                                patient_id varchar(25),
                                event_code varchar(25),
                                event_name varchar(25),
                                event_date date,
                                is_rerun boolean,
                                is_addon boolean
                            );

grant select on table tests.* to 'mysql_reader'@'localhost';

#insert records
insert into dim_lab(lab_id,lab_name) values 
        ('lab1', 'lab1'),
        ('lab2', 'lab2'),
        ('lab3', 'lab3');

insert into dim_hosp(hosp_id, hosp_name) values
        ('hosp1', 'hosp1'),
        ('hosp2', 'hosp2'),
        ('hosp3', 'hosp3');

insert into dim_test_dept(test_dept_id, test_dept_name) values
        ('dept1', 'dept1'),
        ('dept2', 'dept2'),
        ('dept3', 'dept3');

insert into dim_test(test_id, test_name, test_dept_id) values
        ('test1', 'test1', 'dept1'),
        ('test2', 'test2', 'dept2'),
        ('test3', 'test3', 'dept3');

insert into dim_result(result_id, test_id, result_value, result_unit, result_range, result_status) values
        ('result1', 'test1', 'value1', 'unit1', 'range1', 'status1'),
        ('result2', 'test1', 'value2', 'unit2', 'range2', 'status2'),
        ('result3', 'test1', 'value3', 'unit3', 'range3', 'status3'),
        ('result4', 'test2', 'value3', 'unit3', 'range3', 'status3');