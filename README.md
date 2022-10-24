# sheiboi_pytest_POMbased_Allure_report
Python

* Setup Allure on Windows
first exact file > copy or cut it > go to paste C drive > copy bin path add env path

-----------------
install:
----------------
pytest
allure-pytest
pytest-xdist
openpyxl
--------------------

pytest parallel test execution
-------------------------------
pytest-xdist

pytest (location) -v -n 3 --html=report.html

pytest run:
-----------------
pytest -v -s (location)

Run all tests(from all modules)in a path

pytest -v -s (location)D:\Project\Pytest-POM-Boiler-Plate-master\TestCases

pytest -v -s test_LoginLogoutPage.py::test_login
-----------------------------
pytest html report:

pytest (location) -m (single run) --html=report.html

pytest (location) -v --html=report.html

pytest (location) --html=report.html


----------------
Screenshot
-------------
self.driver.save_screenshot(".\\Screenshots"+"test_login.png")

allure run:

pytest --alluredir=report_allure/ .\TestCases\test_LoginLogoutPage.py

pytest -v -s --alluredir="D:\Project\Pytest-POM-Boiler-Plate-master\reports" .\TestCases\test_LoginLogoutPage.py

allure server report_allure/

In command line:
allure serve "" Exact path of report  *******

python -m pytest <filename.py> --alluredir="report path"   ********

python -m allure serve "report path"

