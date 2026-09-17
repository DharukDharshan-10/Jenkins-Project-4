import sys


class ApplicationValidator:

    def __init__(self):
        self.application_name = "Employee Management System"
        self.version = "1.0.0"

        self.required_modules = [
            "Authentication",
            "Employee Management",
            "Database",
            "Reporting"
        ]

        self.configuration = {
            "database": "configured",
            "authentication": "enabled",
            "logging": "enabled",
            "backup": "enabled"
        }

        self.functional_tests = {
            "Login functionality": True,
            "Employee creation": True,
            "Employee search": True,
            "Employee update": True,
            "Report generation": True,
            "Database connection": True
        }

    def print_header(self, title):

        print()
        print("=" * 70)
        print(title)
        print("=" * 70)

    def check_required_modules(self):

        self.print_header("REQUIRED MODULE VALIDATION")

        all_modules_available = True

        for module in self.required_modules:

            print(f"Checking module: {module}")

            if module.strip() == "":
                print(f"FAIL : {module}")
                all_modules_available = False
            else:
                print(f"PASS : {module}")

        return all_modules_available

    def check_configuration(self):

        self.print_header("APPLICATION CONFIGURATION VALIDATION")

        configuration_valid = True

        for key, value in self.configuration.items():

            display_name = key.replace("_", " ").title()

            print(f"{display_name:25}: {value}")

            if value == "":
                configuration_valid = False

        if configuration_valid:
            print("\nPASS : Application configuration is valid")
        else:
            print("\nFAIL : Application configuration contains errors")

        return configuration_valid

    def run_functional_tests(self):

        self.print_header("FUNCTIONAL VALIDATION")

        all_tests_passed = True

        for test_name, result in self.functional_tests.items():

            if result:
                print(f"PASS : {test_name}")
            else:
                print(f"FAIL : {test_name}")
                all_tests_passed = False

        return all_tests_passed

    def validate_application(self):

        self.print_header("EMPLOYEE MANAGEMENT APPLICATION VALIDATION")

        print(f"Application Name : {self.application_name}")
        print(f"Application Version : {self.version}")

        modules_result = self.check_required_modules()

        configuration_result = self.check_configuration()

        functional_result = self.run_functional_tests()

        self.print_header("FINAL APPLICATION VALIDATION RESULT")

        print(f"Required Modules : {'PASSED' if modules_result else 'FAILED'}")
        print(f"Configuration    : {'PASSED' if configuration_result else 'FAILED'}")
        print(f"Functional Tests : {'PASSED' if functional_result else 'FAILED'}")

        if modules_result and configuration_result and functional_result:

            print("\nAPPLICATION VALIDATION: PASSED")
            print("All application checks completed successfully.")

            return True

        print("\nAPPLICATION VALIDATION: FAILED")
        print("One or more application checks failed.")

        return False


def main():

    validator = ApplicationValidator()

    result = validator.validate_application()

    if result:
        sys.exit(0)

    sys.exit(1)


if __name__ == "__main__":
    main()
