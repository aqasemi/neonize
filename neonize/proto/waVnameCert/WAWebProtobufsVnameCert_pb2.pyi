"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class BizAccountLinkInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _AccountType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _AccountTypeEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            BizAccountLinkInfo._AccountType.ValueType
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ENTERPRISE: BizAccountLinkInfo._AccountType.ValueType  # 0

    class AccountType(_AccountType, metaclass=_AccountTypeEnumTypeWrapper): ...
    ENTERPRISE: BizAccountLinkInfo.AccountType.ValueType  # 0

    class _HostStorageType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _HostStorageTypeEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            BizAccountLinkInfo._HostStorageType.ValueType
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ON_PREMISE: BizAccountLinkInfo._HostStorageType.ValueType  # 0
        FACEBOOK: BizAccountLinkInfo._HostStorageType.ValueType  # 1

    class HostStorageType(
        _HostStorageType, metaclass=_HostStorageTypeEnumTypeWrapper
    ): ...
    ON_PREMISE: BizAccountLinkInfo.HostStorageType.ValueType  # 0
    FACEBOOK: BizAccountLinkInfo.HostStorageType.ValueType  # 1

    WHATSAPPBIZACCTFBID_FIELD_NUMBER: builtins.int
    WHATSAPPACCTNUMBER_FIELD_NUMBER: builtins.int
    ISSUETIME_FIELD_NUMBER: builtins.int
    HOSTSTORAGE_FIELD_NUMBER: builtins.int
    ACCOUNTTYPE_FIELD_NUMBER: builtins.int
    whatsappBizAcctFbid: builtins.int
    whatsappAcctNumber: builtins.str
    issueTime: builtins.int
    hostStorage: global___BizAccountLinkInfo.HostStorageType.ValueType
    accountType: global___BizAccountLinkInfo.AccountType.ValueType
    def __init__(
        self,
        *,
        whatsappBizAcctFbid: builtins.int | None = ...,
        whatsappAcctNumber: builtins.str | None = ...,
        issueTime: builtins.int | None = ...,
        hostStorage: global___BizAccountLinkInfo.HostStorageType.ValueType | None = ...,
        accountType: global___BizAccountLinkInfo.AccountType.ValueType | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "accountType",
            b"accountType",
            "hostStorage",
            b"hostStorage",
            "issueTime",
            b"issueTime",
            "whatsappAcctNumber",
            b"whatsappAcctNumber",
            "whatsappBizAcctFbid",
            b"whatsappBizAcctFbid",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "accountType",
            b"accountType",
            "hostStorage",
            b"hostStorage",
            "issueTime",
            b"issueTime",
            "whatsappAcctNumber",
            b"whatsappAcctNumber",
            "whatsappBizAcctFbid",
            b"whatsappBizAcctFbid",
        ],
    ) -> None: ...

global___BizAccountLinkInfo = BizAccountLinkInfo

@typing.final
class BizIdentityInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ActualActorsType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ActualActorsTypeEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            BizIdentityInfo._ActualActorsType.ValueType
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        SELF: BizIdentityInfo._ActualActorsType.ValueType  # 0
        BSP: BizIdentityInfo._ActualActorsType.ValueType  # 1

    class ActualActorsType(
        _ActualActorsType, metaclass=_ActualActorsTypeEnumTypeWrapper
    ): ...
    SELF: BizIdentityInfo.ActualActorsType.ValueType  # 0
    BSP: BizIdentityInfo.ActualActorsType.ValueType  # 1

    class _HostStorageType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _HostStorageTypeEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            BizIdentityInfo._HostStorageType.ValueType
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ON_PREMISE: BizIdentityInfo._HostStorageType.ValueType  # 0
        FACEBOOK: BizIdentityInfo._HostStorageType.ValueType  # 1

    class HostStorageType(
        _HostStorageType, metaclass=_HostStorageTypeEnumTypeWrapper
    ): ...
    ON_PREMISE: BizIdentityInfo.HostStorageType.ValueType  # 0
    FACEBOOK: BizIdentityInfo.HostStorageType.ValueType  # 1

    class _VerifiedLevelValue:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _VerifiedLevelValueEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            BizIdentityInfo._VerifiedLevelValue.ValueType
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: BizIdentityInfo._VerifiedLevelValue.ValueType  # 0
        LOW: BizIdentityInfo._VerifiedLevelValue.ValueType  # 1
        HIGH: BizIdentityInfo._VerifiedLevelValue.ValueType  # 2

    class VerifiedLevelValue(
        _VerifiedLevelValue, metaclass=_VerifiedLevelValueEnumTypeWrapper
    ): ...
    UNKNOWN: BizIdentityInfo.VerifiedLevelValue.ValueType  # 0
    LOW: BizIdentityInfo.VerifiedLevelValue.ValueType  # 1
    HIGH: BizIdentityInfo.VerifiedLevelValue.ValueType  # 2

    VLEVEL_FIELD_NUMBER: builtins.int
    VNAMECERT_FIELD_NUMBER: builtins.int
    SIGNED_FIELD_NUMBER: builtins.int
    REVOKED_FIELD_NUMBER: builtins.int
    HOSTSTORAGE_FIELD_NUMBER: builtins.int
    ACTUALACTORS_FIELD_NUMBER: builtins.int
    PRIVACYMODETS_FIELD_NUMBER: builtins.int
    FEATURECONTROLS_FIELD_NUMBER: builtins.int
    vlevel: global___BizIdentityInfo.VerifiedLevelValue.ValueType
    signed: builtins.bool
    revoked: builtins.bool
    hostStorage: global___BizIdentityInfo.HostStorageType.ValueType
    actualActors: global___BizIdentityInfo.ActualActorsType.ValueType
    privacyModeTS: builtins.int
    featureControls: builtins.int
    @property
    def vnameCert(self) -> global___VerifiedNameCertificate: ...
    def __init__(
        self,
        *,
        vlevel: global___BizIdentityInfo.VerifiedLevelValue.ValueType | None = ...,
        vnameCert: global___VerifiedNameCertificate | None = ...,
        signed: builtins.bool | None = ...,
        revoked: builtins.bool | None = ...,
        hostStorage: global___BizIdentityInfo.HostStorageType.ValueType | None = ...,
        actualActors: global___BizIdentityInfo.ActualActorsType.ValueType | None = ...,
        privacyModeTS: builtins.int | None = ...,
        featureControls: builtins.int | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "actualActors",
            b"actualActors",
            "featureControls",
            b"featureControls",
            "hostStorage",
            b"hostStorage",
            "privacyModeTS",
            b"privacyModeTS",
            "revoked",
            b"revoked",
            "signed",
            b"signed",
            "vlevel",
            b"vlevel",
            "vnameCert",
            b"vnameCert",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "actualActors",
            b"actualActors",
            "featureControls",
            b"featureControls",
            "hostStorage",
            b"hostStorage",
            "privacyModeTS",
            b"privacyModeTS",
            "revoked",
            b"revoked",
            "signed",
            b"signed",
            "vlevel",
            b"vlevel",
            "vnameCert",
            b"vnameCert",
        ],
    ) -> None: ...

global___BizIdentityInfo = BizIdentityInfo

@typing.final
class LocalizedName(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LG_FIELD_NUMBER: builtins.int
    LC_FIELD_NUMBER: builtins.int
    VERIFIEDNAME_FIELD_NUMBER: builtins.int
    lg: builtins.str
    lc: builtins.str
    verifiedName: builtins.str
    def __init__(
        self,
        *,
        lg: builtins.str | None = ...,
        lc: builtins.str | None = ...,
        verifiedName: builtins.str | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "lc", b"lc", "lg", b"lg", "verifiedName", b"verifiedName"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "lc", b"lc", "lg", b"lg", "verifiedName", b"verifiedName"
        ],
    ) -> None: ...

global___LocalizedName = LocalizedName

@typing.final
class VerifiedNameCertificate(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Details(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SERIAL_FIELD_NUMBER: builtins.int
        ISSUER_FIELD_NUMBER: builtins.int
        VERIFIEDNAME_FIELD_NUMBER: builtins.int
        LOCALIZEDNAMES_FIELD_NUMBER: builtins.int
        ISSUETIME_FIELD_NUMBER: builtins.int
        serial: builtins.int
        issuer: builtins.str
        verifiedName: builtins.str
        issueTime: builtins.int
        @property
        def localizedNames(
            self,
        ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
            global___LocalizedName
        ]: ...
        def __init__(
            self,
            *,
            serial: builtins.int | None = ...,
            issuer: builtins.str | None = ...,
            verifiedName: builtins.str | None = ...,
            localizedNames: collections.abc.Iterable[global___LocalizedName]
            | None = ...,
            issueTime: builtins.int | None = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing.Literal[
                "issueTime",
                b"issueTime",
                "issuer",
                b"issuer",
                "serial",
                b"serial",
                "verifiedName",
                b"verifiedName",
            ],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing.Literal[
                "issueTime",
                b"issueTime",
                "issuer",
                b"issuer",
                "localizedNames",
                b"localizedNames",
                "serial",
                b"serial",
                "verifiedName",
                b"verifiedName",
            ],
        ) -> None: ...

    DETAILS_FIELD_NUMBER: builtins.int
    SIGNATURE_FIELD_NUMBER: builtins.int
    SERVERSIGNATURE_FIELD_NUMBER: builtins.int
    details: builtins.bytes
    signature: builtins.bytes
    serverSignature: builtins.bytes
    def __init__(
        self,
        *,
        details: builtins.bytes | None = ...,
        signature: builtins.bytes | None = ...,
        serverSignature: builtins.bytes | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "details",
            b"details",
            "serverSignature",
            b"serverSignature",
            "signature",
            b"signature",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "details",
            b"details",
            "serverSignature",
            b"serverSignature",
            "signature",
            b"signature",
        ],
    ) -> None: ...

global___VerifiedNameCertificate = VerifiedNameCertificate

@typing.final
class BizAccountPayload(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VNAMECERT_FIELD_NUMBER: builtins.int
    BIZACCTLINKINFO_FIELD_NUMBER: builtins.int
    bizAcctLinkInfo: builtins.bytes
    @property
    def vnameCert(self) -> global___VerifiedNameCertificate: ...
    def __init__(
        self,
        *,
        vnameCert: global___VerifiedNameCertificate | None = ...,
        bizAcctLinkInfo: builtins.bytes | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "bizAcctLinkInfo", b"bizAcctLinkInfo", "vnameCert", b"vnameCert"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "bizAcctLinkInfo", b"bizAcctLinkInfo", "vnameCert", b"vnameCert"
        ],
    ) -> None: ...

global___BizAccountPayload = BizAccountPayload
