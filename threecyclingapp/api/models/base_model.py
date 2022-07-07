"""
Contains class BaseModel
"""


class BaseModel():
    """The BaseModel class from which future classes will be derived"""

    def __str__(self):
        """String representation of the class"""
        return "{}".format(self.to_dict())

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of the instance """
        new_dict = self.__dict__.copy()
        if "_state" in new_dict:
            del new_dict["_state"]
        if "password" in new_dict:
            del new_dict["password"]
        return new_dict
