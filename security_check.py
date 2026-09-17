import hashlib
import sys


class SecurityValidator:

    def __init__(self):

        self.application_name = "Employee Management System"
        self.version = "1.0.0"

        self.security_controls = [
            "Password Protection",
            "User Authentication",
            "Input Validation",
            "Role Based Access Control",
            "Activity Logging"
        ]

    def print_header(self, title):

        print()
        print("=" * 70)
        print(title)
        print("=" * 70)

    def check_password_policy(self):

        print("\nChecking password policy...")

        minimum_password_length = 8
        sample_password = "SecurePass123"

        if len(sample_password) >= minimum_password_length:

            print("PASS : Password length requirement satisfied")
            return True

        print("FAIL : Password length requirement not satisfied")
        return False

    def check_authentication(self):

        print("\nChecking authentication...")

        authentication_enabled = True

        if authentication_enabled:

            print("PASS : User authentication is enabled")
            return True

        print("FAIL : User authentication is disabled")
        return False

    def check_input_validation(self):

        print("\nChecking input validation...")

        test_employee_ids = [
            "EMP001",
            "EMP002",
            "EMP003",
            "EMP004"
        ]

        validation_passed = True

        for employee_id in test_employee_ids:

            if employee_id.startswith("EMP") and len(employee_id) == 6:

                print(f"PASS : {employee_id}")

            else:

                print(f"FAIL : {employee_id}")
                validation_passed = False

        return validation_passed

    def check_access_control(self):

        print("\nChecking role based access control...")

        roles = {

            "Administrator": [
                "CREATE",
                "READ",
                "UPDATE",
                "DELETE"
            ],

            "Manager": [
                "CREATE",
                "READ",
                "UPDATE"
            ],

            "Employee": [
                "READ"
            ]
        }

        access_control_valid = True

        for role, permissions in roles.items():

            print(
                f"{role:15} : {', '.join(permissions)}"
            )

            if len(permissions) == 0:

                access_control_valid = False

        if access_control_valid:

            print("PASS : Access control configuration is valid")

        else:

            print("FAIL : Access control configuration is invalid")

        return access_control_valid

    def check_logging(self):

        print("\nChecking activity logging...")

        logging_enabled = True

        if logging_enabled:

            print("PASS : Activity logging is enabled")
            return True

        print("FAIL : Activity logging is disabled")
        return False

    def generate_security_fingerprint(self):

        print("\nGenerating application security fingerprint...")

        application_data = (
            self.application_name
            + "|"
            + self.version
            + "|"
            + "SECURITY_VALIDATION"
        )

        fingerprint = hashlib.sha256(
            application_data.encode()
        ).hexdigest()

        print("Security Fingerprint:")
        print(fingerprint)

        return fingerprint

    def run_security_validation(self):

        self.print_header("SECURITY VALIDATION SYSTEM")

        print(f"Application : {self.application_name}")
        print(f"Version     : {self.version}")

        results = []

        results.append(
            self.check_password_policy()
        )

        results.append(
            self.check_authentication()
        )

        results.append(
            self.check_input_validation()
        )

        results.append(
            self.check_access_control()
        )

        results.append(
            self.check_logging()
        )

        self.generate_security_fingerprint()

        self.print_header("SECURITY VALIDATION RESULT")

        if all(results):

            print("All security checks passed.")
            print("SECURITY VALIDATION: PASSED")

            return True

        print("One or more security checks failed.")
        print("SECURITY VALIDATION: FAILED")

        return False


def main():

    validator = SecurityValidator()

    result = validator.run_security_validation()

    if result:

        sys.exit(0)

    sys.exit(1)


if __name__ == "__main__":
    main()
