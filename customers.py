"""Customers at Hackbright."""


from os import EX_TEMPFAIL, name


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this

    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 password
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return "<Customer: {}, {} >".format(self.first_name, self.last_name)


def read_customer_from_file(filepath):

    customers = {}

    with open(filepath) as file):
        for line in file:
            (first_name,
            last_name,
            email,
            password)=line.strip().split("|")

    return customers

def get_by_email(email):

    return customers[email]
