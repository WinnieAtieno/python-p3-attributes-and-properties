#!/usr/bin/env python3

class Person:
    APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]
    def __init__(self, name = None, job=None):
        self.name = None
        self.job = None
        if name is not None:
            self.set_name(name)
        if job is not None:
            self.set_job(job)

    def set_name(self, name):
        if not isinstance(name, str) or len(name) == 0 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self.name = name.title()

    def set_job(self, job):
        if job not in Person.APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self.job = job
   
guido = Person("Guido","ITC")
print(guido.name)