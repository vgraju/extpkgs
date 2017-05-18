#
# This file is part of pysnmp software.
#
# Copyright (c) 2005-2017, Ilya Etingof <etingof@gmail.com>
# License: http://pysnmp.sf.net/license.html
#
# PySNMP MIB module SNMP-COMMUNITY-MIB (http://pysnmp.sf.net)
# ASN.1 source file:///usr/share/snmp/mibs/SNMP-COMMUNITY-MIB.txt
# Produced by pysmi-0.0.5 at Sat Sep 19 16:28:11 2015
# On host grommit.local platform Darwin version 14.4.0 by user ilya
# Using Python version 2.7.6 (default, Sep  9 2014, 15:04:36) 
#
(Integer, ObjectIdentifier, OctetString,) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier",
                                                                     "OctetString")
(NamedValues,) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
(ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint,
 ValueRangeConstraint,) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint",
                                                   "ConstraintsIntersection", "ValueSizeConstraint",
                                                   "ValueRangeConstraint")
(SnmpAdminString, SnmpEngineID,) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString", "SnmpEngineID")
(snmpTargetAddrEntry, SnmpTagValue,) = mibBuilder.importSymbols("SNMP-TARGET-MIB", "snmpTargetAddrEntry",
                                                                "SnmpTagValue")
(NotificationGroup, ModuleCompliance, ObjectGroup,) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup",
                                                                               "ModuleCompliance", "ObjectGroup")
(Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Bits, TimeTicks,
 Counter64, Unsigned32, ModuleIdentity, Gauge32, snmpModules, iso, ObjectIdentity, IpAddress,
 Counter32,) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow",
                                        "MibTableColumn", "NotificationType", "MibIdentifier", "Bits", "TimeTicks",
                                        "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "snmpModules", "iso",
                                        "ObjectIdentity", "IpAddress", "Counter32")
(StorageType, DisplayString, RowStatus, TextualConvention,) = mibBuilder.importSymbols("SNMPv2-TC", "StorageType",
                                                                                       "DisplayString", "RowStatus",
                                                                                       "TextualConvention")
snmpCommunityMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 18)).setRevisions(("2000-03-06 00:00", "1999-05-13 00:00",))
if mibBuilder.loadTexts:
    snmpCommunityMIB.setLastUpdated('200003060000Z')
if mibBuilder.loadTexts:
    snmpCommunityMIB.setOrganization('SNMPv3 Working Group')
if mibBuilder.loadTexts:
    snmpCommunityMIB.setContactInfo(
        'WG-email:   snmpv3@lists.tislabs.com\n                  Subscribe:  majordomo@lists.tislabs.com\n                              In msg body:  subscribe snmpv3\n\n                  Chair:      Russ Mundy\n                              TIS Labs at Network Associates\n                  Postal:     3060 Washington Rd\n                              Glenwood MD 21738\n                              USA\n                  Email:      mundy@tislabs.com\n                  Phone:      +1-301-854-6889\n\n                  Co-editor:  Rob Frye\n                              CoSine Communications\n                  Postal:     1200 Bridge Parkway\n                              Redwood City, CA 94065\n                              USA\n                  E-mail:     rfrye@cosinecom.com\n                  Phone:      +1 703 725 1130\n\n                  Co-editor:  David B. Levi\n                              Nortel Networks\n                  Postal:     3505 Kesterwood Drive\n                              Knoxville, TN 37918\n                  E-mail:     dlevi@nortelnetworks.com\n                  Phone:      +1 423 686 0432\n\n                  Co-editor:  Shawn A. Routhier\n                              Integrated Systems Inc.\n                  Postal:     333 North Ave 4th Floor\n                              Wakefield, MA 01880\n                  E-mail:     sar@epilogue.com\n                  Phone:      +1 781 245 0804\n\n                  Co-editor:  Bert Wijnen\n                              Lucent Technologies\n                  Postal:     Schagen 33\n                              3461 GL Linschoten\n                              Netherlands\n                  Email:      bwijnen@lucent.com\n                  Phone:      +31-348-407-775\n                 ')
if mibBuilder.loadTexts:
    snmpCommunityMIB.setDescription(
        'This MIB module defines objects to help support coexistence\n             between SNMPv1, SNMPv2c, and SNMPv3.')
snmpCommunityMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 18, 1))
snmpCommunityMIBConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 18, 2))
snmpCommunityTable = MibTable((1, 3, 6, 1, 6, 3, 18, 1, 1), )
if mibBuilder.loadTexts:
    snmpCommunityTable.setDescription(
        "The table of community strings configured in the SNMP\n         engine's Local Configuration Datastore (LCD).")
snmpCommunityEntry = MibTableRow((1, 3, 6, 1, 6, 3, 18, 1, 1, 1), ).setIndexNames(
    (1, "SNMP-COMMUNITY-MIB", "snmpCommunityIndex"))
if mibBuilder.loadTexts:
    snmpCommunityEntry.setDescription('Information about a particular community string.')
snmpCommunityIndex = MibTableColumn((1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 1),
                                    SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts:
    snmpCommunityIndex.setDescription('The unique index value of a row in this table.')
snmpCommunityName = MibTableColumn((1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 2), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    snmpCommunityName.setDescription(
        'The community string for which a row in this table\n         represents a configuration.')
snmpCommunitySecurityName = MibTableColumn((1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 3), SnmpAdminString().subtype(
    subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    snmpCommunitySecurityName.setDescription(
        'A human readable string representing the corresponding\n         value of snmpCommunityName in a Security Model\n         independent format.')
snmpCommunityContextEngineID = MibTableColumn((1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 4), SnmpEngineID()).setMaxAccess(
    "readcreate")
if mibBuilder.loadTexts:
    snmpCommunityContextEngineID.setDescription(
        'The contextEngineID indicating the location of the\n         context in which management information is accessed\n         when using the community string specified by the\n         corresponding instance of snmpCommunityName.\n\n         The default value is the snmpEngineID of the entity in\n         which this object is instantiated.')
snmpCommunityContextName = MibTableColumn((1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 5),
                                          SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(
                                              hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    snmpCommunityContextName.setDescription(
        'The context in which management information is accessed\n         when using the community string specified by the corresponding\n         instance of snmpCommunityName.')
snmpCommunityTransportTag = MibTableColumn((1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 6),
                                           SnmpTagValue().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    snmpCommunityTransportTag.setDescription(
        'This object specifies a set of transport endpoints\n         from which a command responder application will accept\n         management requests.  If a management request containing\n         this community is received on a transport endpoint other\n         than the transport endpoints identified by this object,\n         the request is deemed unauthentic.\n\n         The transports identified by this object are specified\n\n         in the snmpTargetAddrTable.  Entries in that table\n         whose snmpTargetAddrTagList contains this tag value\n         are identified.\n\n         If the value of this object has zero-length, transport\n         endpoints are not checked when authenticating messages\n         containing this community string.')
snmpCommunityStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 7), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    snmpCommunityStorageType.setDescription(
        "The storage type for this conceptual row in the\n         snmpCommunityTable.  Conceptual rows having the value\n         'permanent' need not allow write-access to any\n         columnar object in the row.")
snmpCommunityStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    snmpCommunityStatus.setDescription(
        'The status of this conceptual row in the snmpCommunityTable.\n\n         An entry in this table is not qualified for activation\n         until instances of all corresponding columns have been\n         initialized, either through default values, or through\n         Set operations.  The snmpCommunityName and\n         snmpCommunitySecurityName objects must be explicitly set.\n\n         There is no restriction on setting columns in this table\n         when the value of snmpCommunityStatus is active(1).')
snmpTargetAddrExtTable = MibTable((1, 3, 6, 1, 6, 3, 18, 1, 2), )
if mibBuilder.loadTexts:
    snmpTargetAddrExtTable.setDescription(
        'The table of mask and mms values associated with the\n\n         snmpTargetAddrTable.\n\n         The snmpTargetAddrExtTable augments the\n         snmpTargetAddrTable with a transport address mask value\n         and a maximum message size value.  The transport address\n         mask allows entries in the snmpTargetAddrTable to define\n         a set of addresses instead of just a single address.\n         The maximum message size value allows the maximum\n         message size of another SNMP entity to be configured for\n         use in SNMPv1 (and SNMPv2c) transactions, where the\n         message format does not specify a maximum message size.')
snmpTargetAddrExtEntry = MibTableRow((1, 3, 6, 1, 6, 3, 18, 1, 2, 1), )
snmpTargetAddrEntry.registerAugmentions(("SNMP-COMMUNITY-MIB", "snmpTargetAddrExtEntry"))
snmpTargetAddrExtEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())
if mibBuilder.loadTexts:
    snmpTargetAddrExtEntry.setDescription('Information about a particular mask and mms value.')
snmpTargetAddrTMask = MibTableColumn((1, 3, 6, 1, 6, 3, 18, 1, 2, 1, 1),
                                     OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(
                                         hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    snmpTargetAddrTMask.setDescription(
        'The mask value associated with an entry in the\n         snmpTargetAddrTable.  The value of this object must\n         have the same length as the corresponding instance of\n         snmpTargetAddrTAddress, or must have length 0.  An\n         attempt to set it to any other value will result in\n         an inconsistentValue error.\n\n         The value of this object allows an entry in the\n         snmpTargetAddrTable to specify multiple addresses.\n         The mask value is used to select which bits of\n         a transport address must match bits of the corresponding\n         instance of snmpTargetAddrTAddress, in order for the\n         transport address to match a particular entry in the\n         snmpTargetAddrTable.  Bits which are 1 in the mask\n         value indicate bits in the transport address which\n         must match bits in the snmpTargetAddrTAddress value.\n\n         Bits which are 0 in the mask indicate bits in the\n         transport address which need not match.  If the\n         length of the mask is 0, the mask should be treated\n         as if all its bits were 1 and its length were equal\n         to the length of the corresponding value of\n         snmpTargetAddrTable.\n\n         This object may not be modified while the value of the\n         corresponding instance of snmpTargetAddrRowStatus is\n         active(1).  An attempt to set this object in this case\n         will result in an inconsistentValue error.')
snmpTargetAddrMMS = MibTableColumn((1, 3, 6, 1, 6, 3, 18, 1, 2, 1, 2), Integer32().subtype(
    subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(484, 2147483647), )).clone(
    484)).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    snmpTargetAddrMMS.setDescription(
        'The maximum message size value associated with an entry\n         in the snmpTargetAddrTable.')
snmpTrapAddress = MibScalar((1, 3, 6, 1, 6, 3, 18, 1, 3), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts:
    snmpTrapAddress.setDescription(
        'The value of the agent-addr field of a Trap PDU which\n         is forwarded by a proxy forwarder application using\n         an SNMP version other than SNMPv1.  The value of this\n         object SHOULD contain the value of the agent-addr field\n         from the original Trap PDU as generated by an SNMPv1\n         agent.')
snmpTrapCommunity = MibScalar((1, 3, 6, 1, 6, 3, 18, 1, 4), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setDescription(
        'The value of the community string field of an SNMPv1\n         message containing a Trap PDU which is forwarded by a\n         a proxy forwarder application using an SNMP version\n         other than SNMPv1.  The value of this object SHOULD\n         contain the value of the community string field from\n         the original SNMPv1 message containing a Trap PDU as\n         generated by an SNMPv1 agent.')
snmpCommunityMIBCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 18, 2, 1))
snmpCommunityMIBGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 18, 2, 2))
snmpCommunityMIBCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 18, 2, 1, 1)).setObjects(
    *(("SNMP-COMMUNITY-MIB", "snmpCommunityGroup"),))
if mibBuilder.loadTexts:
    snmpCommunityMIBCompliance.setDescription(
        'The compliance statement for SNMP engines which\n         implement the SNMP-COMMUNITY-MIB.')
snmpProxyTrapForwardCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 18, 2, 1, 2)).setObjects(
    *(("SNMP-COMMUNITY-MIB", "snmpProxyTrapForwardGroup"),))
if mibBuilder.loadTexts:
    snmpProxyTrapForwardCompliance.setDescription(
        'The compliance statement for SNMP engines which\n         contain a proxy forwarding application which is\n         capable of forwarding SNMPv1 traps using SNMPv2c\n         or SNMPv3.')
snmpCommunityGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 18, 2, 2, 1)).setObjects(
    *(("SNMP-COMMUNITY-MIB", "snmpCommunityName"), ("SNMP-COMMUNITY-MIB", "snmpCommunitySecurityName"),
      ("SNMP-COMMUNITY-MIB", "snmpCommunityContextEngineID"), ("SNMP-COMMUNITY-MIB", "snmpCommunityContextName"),
      ("SNMP-COMMUNITY-MIB", "snmpCommunityTransportTag"), ("SNMP-COMMUNITY-MIB", "snmpCommunityStorageType"),
      ("SNMP-COMMUNITY-MIB", "snmpCommunityStatus"), ("SNMP-COMMUNITY-MIB", "snmpTargetAddrTMask"),
      ("SNMP-COMMUNITY-MIB", "snmpTargetAddrMMS"))
)
if mibBuilder.loadTexts:
    snmpCommunityGroup.setDescription(
        'A collection of objects providing for configuration\n         of community strings for SNMPv1 (and SNMPv2c) usage.')
snmpProxyTrapForwardGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 18, 2, 2, 3)).setObjects(
    *(("SNMP-COMMUNITY-MIB", "snmpTrapAddress"), ("SNMP-COMMUNITY-MIB", "snmpTrapCommunity"),))
if mibBuilder.loadTexts:
    snmpProxyTrapForwardGroup.setDescription(
        'Objects which are used by proxy forwarding applications\n         when translating traps between SNMP versions.  These are\n         used to preserve SNMPv1-specific information when\n\n         translating to SNMPv2c or SNMPv3.')
mibBuilder.exportSymbols("SNMP-COMMUNITY-MIB", snmpCommunityContextName=snmpCommunityContextName,
                         snmpCommunityMIBConformance=snmpCommunityMIBConformance, snmpCommunityName=snmpCommunityName,
                         PYSNMP_MODULE_ID=snmpCommunityMIB, snmpCommunityMIBCompliance=snmpCommunityMIBCompliance,
                         snmpCommunityContextEngineID=snmpCommunityContextEngineID,
                         snmpCommunityEntry=snmpCommunityEntry, snmpCommunityMIBGroups=snmpCommunityMIBGroups,
                         snmpCommunityMIB=snmpCommunityMIB, snmpCommunitySecurityName=snmpCommunitySecurityName,
                         snmpProxyTrapForwardCompliance=snmpProxyTrapForwardCompliance,
                         snmpCommunityTransportTag=snmpCommunityTransportTag,
                         snmpTargetAddrExtTable=snmpTargetAddrExtTable, snmpCommunityMIBObjects=snmpCommunityMIBObjects,
                         snmpTrapAddress=snmpTrapAddress, snmpCommunityMIBCompliances=snmpCommunityMIBCompliances,
                         snmpCommunityIndex=snmpCommunityIndex, snmpCommunityGroup=snmpCommunityGroup,
                         snmpTrapCommunity=snmpTrapCommunity, snmpCommunityStorageType=snmpCommunityStorageType,
                         snmpTargetAddrTMask=snmpTargetAddrTMask, snmpCommunityTable=snmpCommunityTable,
                         snmpTargetAddrExtEntry=snmpTargetAddrExtEntry, snmpCommunityStatus=snmpCommunityStatus,
                         snmpProxyTrapForwardGroup=snmpProxyTrapForwardGroup, snmpTargetAddrMMS=snmpTargetAddrMMS)
