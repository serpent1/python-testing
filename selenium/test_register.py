from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
import os
from time import sleep
import pytest


class Test_regieter_form:

    @pytest.mark.parametrize("name, email,gender", [('testname', 'test@test.com', 'female'),
                                                    ('testname', 'test@test.com', 'male'),
                                                    ('testname', 'test@test.com', 'others'),
                                                    pytest.param('testname', 'test@test.com', '',
                                                                 marks=pytest.mark.xfail(reason='gender null')),
                                                    pytest.param('testname', '', 'female',
                                                                 marks=pytest.mark.xfail(reason='email null')),
                                                    pytest.param('', 'test@test.com', 'female',
                                                                 marks=pytest.mark.xfail(reason='name null')),
                                                    pytest.param('testname', '', '',
                                                                 marks=pytest.mark.xfail(reason='gender and email null')),
                                                    pytest.param('', 'test@test.com', '',
                                                                 marks=pytest.mark.xfail(reason='gender and name null')),
                                                    pytest.param('', '', 'female',
                                                                 marks=pytest.mark.xfail(reason='name and email null')),
                                                    pytest.param('', '', '',
                                                                 marks=pytest.mark.xfail(reason='all params null')),

                                                    ]
                             )
    def test_register(self, launch_broswer, name, email, gender, ):

        _name = launch_broswer.find_element(By.ID, 'name')
        _name.send_keys(name)
        sleep(2)

        _email = launch_broswer.find_element(By.ID, 'email')
        _email.send_keys(email)
        sleep(2)
        if gender == 'female':
            _female = launch_broswer.find_element(By.ID, 'female')
            _female.click()
            sleep(2)
        elif gender == 'male':
            male = launch_broswer.find_element(By.ID, 'male')
            male.click()
            sleep(2)
        elif gender == 'others':
            others = launch_broswer.find_element(By.ID, 'others')
            others.click()
            sleep(2)
        else:
            pass

        _submit = launch_broswer.find_element(By.TAG_NAME, 'button')
        _submit.click()
        try:
            _alert = launch_broswer.switch_to.alert
            _alertText=_alert.text
            assert _alertText=='You have submitted the application form.'
        except NoAlertPresentException:
            pass




if __name__ == "__main__":
    pytest.main(["-s", "test_register.py"])
