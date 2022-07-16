import pytest
from controller.controller import read_file, list_employee, compare_schedule
from model.model import Employee


def test_compare_schedule_when_first_employee_dont_coincide_at_office():
    first_checkin = "10:00"
    first_checkout = "12:00"
    second_checkin = "13:00"
    second_checkout = "15:00"
    TEST_VALUE = compare_schedule(
        first_checkin, first_checkout, second_checkin, second_checkout)
    EXPECTED_VALUE = False

    assert TEST_VALUE == EXPECTED_VALUE


def test_compare_schedule_when_second_checkin_is_lower_than_first_checkout():
    first_checkin = "10:00"
    first_checkout = "12:00"
    second_checkin = "11:59"
    second_checkout = "15:00"
    TEST_VALUE = compare_schedule(
        first_checkin, first_checkout, second_checkin, second_checkout)
    EXPECTED_VALUE = True

    assert TEST_VALUE == EXPECTED_VALUE


def test_compare_schedule_when_first_employee_schedule_is_between_second_employee_schedule():
    first_checkin = "10:00"
    first_checkout = "12:00"
    second_checkin = "09:00"
    second_checkout = "15:00"
    TEST_VALUE = compare_schedule(
        first_checkin, first_checkout, second_checkin, second_checkout)
    EXPECTED_VALUE = True

    assert TEST_VALUE == EXPECTED_VALUE


def test_compare_schedule_when_second_employee_schedule_is_between_first_employee_schedule():
    first_checkin = "08:00"
    first_checkout = "12:00"
    second_checkin = "09:00"
    second_checkout = "11:00"
    TEST_VALUE = compare_schedule(
        first_checkin, first_checkout, second_checkin, second_checkout)
    EXPECTED_VALUE = True

    assert TEST_VALUE == EXPECTED_VALUE
