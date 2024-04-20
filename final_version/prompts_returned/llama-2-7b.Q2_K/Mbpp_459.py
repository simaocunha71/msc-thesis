"""
Write a function to remove uppercase substrings from a given string.
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
"""
from typing import Any, Dict, List, Optional, Set, Type, Union  # noqa: F401
from azure.core.paging import ItemPaged, Pageable, ResourceList
from azure.core.tracing.decorator_async import distributed_trace
from azure.mgmt.containerservice.models import (
    AzureFileShareReadOnlyAccessControl, ContributorAccessControlEntry,
)
from azure.mgmt.containerservice.models import (
    ContainerDeleteOptions, CreateMode, FileDeleteOption, ListContainerSnapshotsOptionalParams,
    ListContainersOptionalParams, ListLogsOptionalParams, ListSharesOptionalParams, PagedEtagList,
    ShareCreateOptions, ShareProperties, UpdateMode, UpdateShareOptions, WriteOnlyAccessControlEntry,
)
from azure.mgmt.containerservice import ContainersASMXClient
from msrest import Serializer


def _list_shares_to_return(client: "ContainersASMXClient") -> List[ShareProperties]:
    shares = []
    while True:
        page = client.get_all_my_namespaces(
            resource_type="Share"
        )
        for share in page.content:
            shares.append(share.properties)
        if not page.next_link:
            break

    return shares


def _list_fileshares_to_return(client, account_name):  # pylint: disable=inheritance-misplaced-with-origin
    sharename = f"{account_name}.file.core.windows.net/{}".format("container")
    shares = []
    while True:
        page = client.list_fileshares(sharename)
        for fileshare in page.value:
            shares.append(fileshare.properties)
        if not page.next_link:
            break

    return shares


def _get_share(client, account_name):  # pylint: disable=inheritance-misplaced-with-origin
    sharename = f"{account_name}.file.core.windows