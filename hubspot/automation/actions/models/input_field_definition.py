# coding: utf-8

"""
    Custom Workflow Actions

    Create custom workflow actions  # noqa: E501

    The version of the OpenAPI document: v4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.automation.actions.configuration import Configuration


class InputFieldDefinition(object):
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
    openapi_types = {"type_definition": "FieldTypeDefinition", "supported_value_types": "list[str]", "is_required": "bool"}

    attribute_map = {"type_definition": "typeDefinition", "supported_value_types": "supportedValueTypes", "is_required": "isRequired"}

    def __init__(self, type_definition=None, supported_value_types=None, is_required=None, local_vars_configuration=None):  # noqa: E501
        """InputFieldDefinition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type_definition = None
        self._supported_value_types = None
        self._is_required = None
        self.discriminator = None

        self.type_definition = type_definition
        if supported_value_types is not None:
            self.supported_value_types = supported_value_types
        self.is_required = is_required

    @property
    def type_definition(self):
        """Gets the type_definition of this InputFieldDefinition.  # noqa: E501


        :return: The type_definition of this InputFieldDefinition.  # noqa: E501
        :rtype: FieldTypeDefinition
        """
        return self._type_definition

    @type_definition.setter
    def type_definition(self, type_definition):
        """Sets the type_definition of this InputFieldDefinition.


        :param type_definition: The type_definition of this InputFieldDefinition.  # noqa: E501
        :type: FieldTypeDefinition
        """
        if self.local_vars_configuration.client_side_validation and type_definition is None:  # noqa: E501
            raise ValueError("Invalid value for `type_definition`, must not be `None`")  # noqa: E501

        self._type_definition = type_definition

    @property
    def supported_value_types(self):
        """Gets the supported_value_types of this InputFieldDefinition.  # noqa: E501

        Controls what kind of input a customer can use to specify the field value. Must contain exactly one of `STATIC_VALUE` or `OBJECT_PROPERTY`. If `STATIC_VALUE`, the customer will be able to choose a value when configuring the custom action; if `OBJECT_PROPERTY`, the customer will be able to choose a property from the enrolled workflow object that the field value will be copied from. In the future we may support more than one input control type here.  # noqa: E501

        :return: The supported_value_types of this InputFieldDefinition.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_value_types

    @supported_value_types.setter
    def supported_value_types(self, supported_value_types):
        """Sets the supported_value_types of this InputFieldDefinition.

        Controls what kind of input a customer can use to specify the field value. Must contain exactly one of `STATIC_VALUE` or `OBJECT_PROPERTY`. If `STATIC_VALUE`, the customer will be able to choose a value when configuring the custom action; if `OBJECT_PROPERTY`, the customer will be able to choose a property from the enrolled workflow object that the field value will be copied from. In the future we may support more than one input control type here.  # noqa: E501

        :param supported_value_types: The supported_value_types of this InputFieldDefinition.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["STATIC_VALUE", "OBJECT_PROPERTY", "FIELD_DATA"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and not set(supported_value_types).issubset(set(allowed_values)):  # noqa: E501
            raise ValueError(
                "Invalid values for `supported_value_types` [{0}], must be a subset of [{1}]".format(  # noqa: E501
                    ", ".join(map(str, set(supported_value_types) - set(allowed_values))), ", ".join(map(str, allowed_values))  # noqa: E501
                )
            )

        self._supported_value_types = supported_value_types

    @property
    def is_required(self):
        """Gets the is_required of this InputFieldDefinition.  # noqa: E501

        Whether the field is required for the custom action to be valid  # noqa: E501

        :return: The is_required of this InputFieldDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """Sets the is_required of this InputFieldDefinition.

        Whether the field is required for the custom action to be valid  # noqa: E501

        :param is_required: The is_required of this InputFieldDefinition.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_required is None:  # noqa: E501
            raise ValueError("Invalid value for `is_required`, must not be `None`")  # noqa: E501

        self._is_required = is_required

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
        if not isinstance(other, InputFieldDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputFieldDefinition):
            return True

        return self.to_dict() != other.to_dict()