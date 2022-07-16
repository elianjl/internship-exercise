import pytest
from controller.controller import read_file, list_employee, compare_schedule
from model.model import Employee


def test_read_file_when_file_name_doesnt_exist():
    file_name = "data/data.txt"
    TEST_VALUE = read_file(file_name)
    EXPECTED_VALUE = None

    assert TEST_VALUE == EXPECTED_VALUE


def test_read_file_when_file_name_exist():
    file_name = "data/data_employees.txt"
    TEST_VALUE = read_file(file_name)
    EXPECTED_VALUE = ["RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n",
                      "ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00\n",
                      "ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00\n",
                      "JULIA=MO10:15-13:00,TU10:15-12:15,SA17:15-20:00,SU21:15-22:00\n",
                      "LUKE=MO14:00-16:00,TU10:30-12:30,SA17:30-21:30,SU20:00-21:00"]

    assert TEST_VALUE == EXPECTED_VALUE


def test_list_employee_when_lines_have_different_format():
    lines = ["abc", "123", "xyz", ""]
    TEST_VALUE = list_employee(lines)
    EXPECTED_VALUE = None

    assert TEST_VALUE == EXPECTED_VALUE


def test_compare_schedule_when_first_employee_dont_coincide_at_office():
    first_checkin = "10:00"
    first_checkout = "12:00"
    second_checkin = "13:00"
    second_checkout = "15:00"
    TEST_VALUE = compare_schedule(first_checkin, first_checkout, second_checkin, second_checkout)
    EXPECTED_VALUE = False

    assert TEST_VALUE == EXPECTED_VALUE


def test_compare_schedule_when_second_checkin_is_lower_than_first_checkout():
    first_checkin = "10:00"
    first_checkout = "12:00"
    second_checkin = "11:59"
    second_checkout = "15:00"
    TEST_VALUE = compare_schedule(first_checkin, first_checkout, second_checkin, second_checkout)
    EXPECTED_VALUE = True

    assert TEST_VALUE == EXPECTED_VALUE


def test_compare_schedule_when_first_employee_schedule_is_between_second_employee_schedule():
    first_checkin = "10:00"
    first_checkout = "12:00"
    second_checkin = "09:00"
    second_checkout = "15:00"
    TEST_VALUE = compare_schedule(first_checkin, first_checkout, second_checkin, second_checkout)
    EXPECTED_VALUE = True

    assert TEST_VALUE == EXPECTED_VALUE


def test_compare_schedule_when_second_employee_schedule_is_between_first_employee_schedule():
    first_checkin = "08:00"
    first_checkout = "12:00"
    second_checkin = "09:00"
    second_checkout = "11:00"
    TEST_VALUE = compare_schedule(first_checkin, first_checkout, second_checkin, second_checkout)
    EXPECTED_VALUE = True

    assert TEST_VALUE == EXPECTED_VALUE
