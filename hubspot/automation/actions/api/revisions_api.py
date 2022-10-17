# coding: utf-8

"""
    Custom Workflow Actions

    Create custom workflow actions  # noqa: E501

    The version of the OpenAPI document: v4
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.automation.actions.api_client import ApiClient
from hubspot.automation.actions.exceptions import ApiTypeError, ApiValueError


class RevisionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_by_id(self, definition_id, revision_id, app_id, **kwargs):  # noqa: E501
        """Get a revision for a custom action  # noqa: E501

        Returns the given version of a custom workflow action.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id(definition_id, revision_id, app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str definition_id: The ID of the custom workflow action. (required)
        :param str revision_id: The version of the custom workflow action. (required)
        :param int app_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ActionRevision
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_by_id_with_http_info(definition_id, revision_id, app_id, **kwargs)  # noqa: E501

    def get_by_id_with_http_info(self, definition_id, revision_id, app_id, **kwargs):  # noqa: E501
        """Get a revision for a custom action  # noqa: E501

        Returns the given version of a custom workflow action.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id_with_http_info(definition_id, revision_id, app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str definition_id: The ID of the custom workflow action. (required)
        :param str revision_id: The version of the custom workflow action. (required)
        :param int app_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ActionRevision, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["definition_id", "revision_id", "app_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_by_id" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'definition_id' is set
        if self.api_client.client_side_validation and ("definition_id" not in local_var_params or local_var_params["definition_id"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `definition_id` when calling `get_by_id`")  # noqa: E501
        # verify the required parameter 'revision_id' is set
        if self.api_client.client_side_validation and ("revision_id" not in local_var_params or local_var_params["revision_id"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `revision_id` when calling `get_by_id`")  # noqa: E501
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ("app_id" not in local_var_params or local_var_params["app_id"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `get_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "definition_id" in local_var_params:
            path_params["definitionId"] = local_var_params["definition_id"]  # noqa: E501
        if "revision_id" in local_var_params:
            path_params["revisionId"] = local_var_params["revision_id"]  # noqa: E501
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["developer_hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/automation/v4/actions/{appId}/{definitionId}/revisions/{revisionId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ActionRevision",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_page(self, definition_id, app_id, **kwargs):  # noqa: E501
        """Get all revisions for a custom action  # noqa: E501

        Returns a list of revisions for a custom workflow action.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_page(definition_id, app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str definition_id: The ID of the custom workflow action (required)
        :param int app_id: (required)
        :param int limit: Maximum number of results per page.
        :param str after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CollectionResponseActionRevisionForwardPaging
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_page_with_http_info(definition_id, app_id, **kwargs)  # noqa: E501

    def get_page_with_http_info(self, definition_id, app_id, **kwargs):  # noqa: E501
        """Get all revisions for a custom action  # noqa: E501

        Returns a list of revisions for a custom workflow action.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_page_with_http_info(definition_id, app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str definition_id: The ID of the custom workflow action (required)
        :param int app_id: (required)
        :param int limit: Maximum number of results per page.
        :param str after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CollectionResponseActionRevisionForwardPaging, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["definition_id", "app_id", "limit", "after"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_page" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'definition_id' is set
        if self.api_client.client_side_validation and ("definition_id" not in local_var_params or local_var_params["definition_id"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `definition_id` when calling `get_page`")  # noqa: E501
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ("app_id" not in local_var_params or local_var_params["app_id"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `get_page`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "definition_id" in local_var_params:
            path_params["definitionId"] = local_var_params["definition_id"]  # noqa: E501
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

        query_params = []
        if "limit" in local_var_params and local_var_params["limit"] is not None:  # noqa: E501
            query_params.append(("limit", local_var_params["limit"]))  # noqa: E501
        if "after" in local_var_params and local_var_params["after"] is not None:  # noqa: E501
            query_params.append(("after", local_var_params["after"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["developer_hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/automation/v4/actions/{appId}/{definitionId}/revisions",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="CollectionResponseActionRevisionForwardPaging",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )