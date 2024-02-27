from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class LoggingApplication:
    def __init__(self, logger: Logger):
        self.logger = logger

    def perform_action(self):
        # Dummy action
        self.logger.log("Action performed successfully.")

class SpecificLogger(Logger):
    def log(self, message):
        print(f"Logging: {message}")

class AnotherLogger(Logger):
    def log(self, message):
        print(f"Another Logging: {message}")

def main():
    # Creating instances of loggers
    specific_logger = SpecificLogger()
    another_logger = AnotherLogger()

    # Creating instance of LoggingApplication with SpecificLogger
    app = LoggingApplication(specific_logger)
    app.perform_action()

    # Creating instance of LoggingApplication with AnotherLogger
    app_with_another_logger = LoggingApplication(another_logger)
    app_with_another_logger.perform_action()

if __name__ == "__main__":
    main()
