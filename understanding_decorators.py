def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper function executed ahead of {original_function.__name__}")
        return original_function(*args, **kwargs)

    return wrapper_function


class DecoratorClass:
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f"Call function executed ahead of {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)


@decorator_function
def display_info(name, age):
    print(f"Name: {name}\nAge: {age}\n")


@DecoratorClass
def display_class(grade, section):
    print(f"Grade: {grade}\nSection: {section}\n")


display_info("Suyog", 22)
display_class(10, "C")
