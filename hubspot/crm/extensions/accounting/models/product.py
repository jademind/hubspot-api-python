# coding: utf-8

"""
    Accounting Extension

    These APIs allow you to interact with HubSpot's Accounting Extension. It allows you to: * Specify the URLs that HubSpot will use when making webhook requests to your external accounting system. * Respond to webhook calls made to your external accounting system by HubSpot   # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.extensions.accounting.configuration import Configuration


class Product(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"unit_price": "UnitPrice", "tax_exempt": "bool", "sales_tax_type": "TaxType", "name": "str", "description": "str", "id": "str"}

    attribute_map = {"unit_price": "unitPrice", "tax_exempt": "taxExempt", "sales_tax_type": "salesTaxType", "name": "name", "description": "description", "id": "id"}

    def __init__(self, unit_price=None, tax_exempt=None, sales_tax_type=None, name=None, description=None, id=None, local_vars_configuration=None):  # noqa: E501
        """Product - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._unit_price = None
        self._tax_exempt = None
        self._sales_tax_type = None
        self._name = None
        self._description = None
        self._id = None
        self.discriminator = None

        self.unit_price = unit_price
        self.tax_exempt = tax_exempt
        if sales_tax_type is not None:
            self.sales_tax_type = sales_tax_type
        self.name = name
        if description is not None:
            self.description = description
        self.id = id

    @property
    def unit_price(self):
        """Gets the unit_price of this Product.  # noqa: E501


        :return: The unit_price of this Product.  # noqa: E501
        :rtype: UnitPrice
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this Product.


        :param unit_price: The unit_price of this Product.  # noqa: E501
        :type: UnitPrice
        """
        if self.local_vars_configuration.client_side_validation and unit_price is None:  # noqa: E501
            raise ValueError("Invalid value for `unit_price`, must not be `None`")  # noqa: E501

        self._unit_price = unit_price

    @property
    def tax_exempt(self):
        """Gets the tax_exempt of this Product.  # noqa: E501

        Identifies if the product is tax exempt or not.  # noqa: E501

        :return: The tax_exempt of this Product.  # noqa: E501
        :rtype: bool
        """
        return self._tax_exempt

    @tax_exempt.setter
    def tax_exempt(self, tax_exempt):
        """Sets the tax_exempt of this Product.

        Identifies if the product is tax exempt or not.  # noqa: E501

        :param tax_exempt: The tax_exempt of this Product.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and tax_exempt is None:  # noqa: E501
            raise ValueError("Invalid value for `tax_exempt`, must not be `None`")  # noqa: E501

        self._tax_exempt = tax_exempt

    @property
    def sales_tax_type(self):
        """Gets the sales_tax_type of this Product.  # noqa: E501


        :return: The sales_tax_type of this Product.  # noqa: E501
        :rtype: TaxType
        """
        return self._sales_tax_type

    @sales_tax_type.setter
    def sales_tax_type(self, sales_tax_type):
        """Sets the sales_tax_type of this Product.


        :param sales_tax_type: The sales_tax_type of this Product.  # noqa: E501
        :type: TaxType
        """

        self._sales_tax_type = sales_tax_type

    @property
    def name(self):
        """Gets the name of this Product.  # noqa: E501

        The display name of the product.  # noqa: E501

        :return: The name of this Product.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Product.

        The display name of the product.  # noqa: E501

        :param name: The name of this Product.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Product.  # noqa: E501

        The description of the product.  # noqa: E501

        :return: The description of this Product.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Product.

        The description of the product.  # noqa: E501

        :param description: The description of this Product.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Product.  # noqa: E501

        The ID of the product in the external accounting system.  # noqa: E501

        :return: The id of this Product.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Product.

        The ID of the product in the external accounting system.  # noqa: E501

        :param id: The id of this Product.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item, value.items()))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Product):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Product):
            return True

        return self.to_dict() != other.to_dict()