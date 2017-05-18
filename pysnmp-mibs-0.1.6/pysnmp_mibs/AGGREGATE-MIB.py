#
# PySNMP MIB module AGGREGATE-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/AGGREGATE-MIB
# Produced by pysmi-0.0.7 at Sun Feb 14 00:04:25 2016
# On host bldfarm platform Linux version 4.1.13-100.fc21.x86_64 by user goose
# Using Python version 3.5.0 (default, Jan  5 2016, 17:11:52) 
#
( ObjectIdentifier, Integer, OctetString, ) = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
( OwnerString, ) = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( NotificationGroup, ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
( ModuleIdentity, IpAddress, Bits, Gauge32, Opaque, experimental, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, Counter64, MibIdentifier, ObjectIdentity, NotificationType, TimeTicks, Unsigned32, Integer32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Opaque", "experimental", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "Counter64", "MibIdentifier", "ObjectIdentity", "NotificationType", "TimeTicks", "Unsigned32", "Integer32")
( TextualConvention, DisplayString, RowStatus, StorageType, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "StorageType")
aggrMIB = ModuleIdentity((1, 3, 6, 1, 3, 123)).setRevisions(("2006-04-27 00:00",))
if mibBuilder.loadTexts: aggrMIB.setLastUpdated('200604270000Z')
if mibBuilder.loadTexts: aggrMIB.setOrganization('Cyber Solutions Inc. NetMan Working Group')
if mibBuilder.loadTexts: aggrMIB.setContactInfo('                      Glenn Mansfield Keeni\n                     Postal: Cyber Solutions Inc.\n                             6-6-3, Minami Yoshinari\n                             Aoba-ku, Sendai, Japan 989-3204.\n                        Tel: +81-22-303-4012\n                        Fax: +81-22-303-4015\n                     E-mail: glenn@cysols.com\n\n          Support Group E-mail: mibsupport@cysols.com')
if mibBuilder.loadTexts: aggrMIB.setDescription('The MIB for servicing aggregate objects.\n\n                   Copyright (C) The Internet Society (2006).  This\n                   version of this MIB module is part of RFC 4498;\n                   see the RFC itself for full legal notices.\n                  ')
class AggrMOErrorStatus(Opaque, TextualConvention):
    subtypeSpec = Opaque.subtypeSpec+ValueSizeConstraint(0,1024)

class AggrMOValue(Opaque, TextualConvention):
    subtypeSpec = Opaque.subtypeSpec+ValueSizeConstraint(0,1024)

class AggrMOCompressedValue(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,1024)

aggrCtlTable = MibTable((1, 3, 6, 1, 3, 123, 1), )
if mibBuilder.loadTexts: aggrCtlTable.setDescription('A table that controls the aggregation of the MOs.')
aggrCtlEntry = MibTableRow((1, 3, 6, 1, 3, 123, 1, 1), ).setIndexNames((0, "AGGREGATE-MIB", "aggrCtlEntryID"))
if mibBuilder.loadTexts: aggrCtlEntry.setDescription('A row of the control table that defines one aggregated\n           MO.\n\n\n\n\n\n           Entries in this table are required to survive a reboot\n           of the managed entity depending on the value of the\n           corresponding aggrCtlEntryStorageType instance.\n          ')
aggrCtlEntryID = MibTableColumn((1, 3, 6, 1, 3, 123, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1,32)))
if mibBuilder.loadTexts: aggrCtlEntryID.setDescription('A locally unique, administratively assigned name\n           for this aggregated MO.  It is used as an index to\n           uniquely identify this row in the table.')
aggrCtlMOIndex = MibTableColumn((1, 3, 6, 1, 3, 123, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrCtlMOIndex.setDescription('A pointer to a group of MOs identified by aggrMOEntryID\n           in the aggrMOTable.  This is the group of MOs that will\n           be aggregated.')
aggrCtlMODescr = MibTableColumn((1, 3, 6, 1, 3, 123, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0,64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrCtlMODescr.setDescription('A textual description of the object that is\n           being aggregated.')
aggrCtlCompressionAlgorithm = MibTableColumn((1, 3, 6, 1, 3, 123, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2,))).clone(namedValues=NamedValues(("none", 1), ("deflate", 2),)).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrCtlCompressionAlgorithm.setDescription('The compression algorithm that will be used by\n           the agent to compress the value of the aggregated\n           object.\n           The deflate algorithm and corresponding data format\n           specification is described in RFC 1951.  It is\n           compatible with the widely used gzip utility.\n          ')
aggrCtlEntryOwner = MibTableColumn((1, 3, 6, 1, 3, 123, 1, 1, 5), OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrCtlEntryOwner.setDescription('The entity that created this entry.')
aggrCtlEntryStorageType = MibTableColumn((1, 3, 6, 1, 3, 123, 1, 1, 6), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrCtlEntryStorageType.setDescription("This object defines whether the parameters defined in\n            this row are kept in volatile storage and lost upon\n            reboot or backed up by non-volatile (permanent)\n            storage.\n\n            Conceptual rows having the value 'permanent' need not\n            allow write-access to any columnar objects in the row.\n\n\n\n           ")
aggrCtlEntryStatus = MibTableColumn((1, 3, 6, 1, 3, 123, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrCtlEntryStatus.setDescription("The row status variable, used according to row\n            installation and removal conventions.\n            Objects in a row can be modified only when the value of\n            this object in the corresponding conceptual row is not\n            'active'.\n            Thus, to modify one or more of the objects in this\n            conceptual row,\n              a. change the row status to 'notInService',\n              b. change the values of the row, and\n              c. change the row status to 'active'.\n            The aggrCtlEntryStatus may be changed to 'active' if\n            all the MOs in the conceptual row have been assigned\n            valid values.\n           ")
aggrMOTable = MibTable((1, 3, 6, 1, 3, 123, 2), )
if mibBuilder.loadTexts: aggrMOTable.setDescription('The table of primary(simple) MOs that will be aggregated.\n            Each row in this table represents a MO that will be\n            aggregated.  The aggrMOEntryID index is used to identify\n            the group of MOs that will be aggregated.  The\n            aggrMOIndex instance in the corresponding row of the\n            aggrCtlTable will have a value equal to the value of\n            aggrMOEntryID.  The aggrMOEntryMOID index is used to\n            identify an MO in the group.\n           ')
aggrMOEntry = MibTableRow((1, 3, 6, 1, 3, 123, 2, 1), ).setIndexNames((0, "AGGREGATE-MIB", "aggrMOEntryID"), (0, "AGGREGATE-MIB", "aggrMOEntryMOID"))
if mibBuilder.loadTexts: aggrMOEntry.setDescription('A row of the table that specifies one MO.\n            Entries in this table are required to survive a reboot\n            of the managed entity depending on the value of the\n            corresponding aggrMOEntryStorageType instance.\n           ')
aggrMOEntryID = MibTableColumn((1, 3, 6, 1, 3, 123, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647)))
if mibBuilder.loadTexts: aggrMOEntryID.setDescription('An index uniquely identifying a group of MOs\n           that will be aggregated.')
aggrMOEntryMOID = MibTableColumn((1, 3, 6, 1, 3, 123, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1,65535)))
if mibBuilder.loadTexts: aggrMOEntryMOID.setDescription('An index to uniquely identify an MO instance in the\n           group of MO instances that will be aggregated.')
aggrMOInstance = MibTableColumn((1, 3, 6, 1, 3, 123, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrMOInstance.setDescription('The OID of the MO instance, the value of which will\n           be sampled by the agent.')
aggrMODescr = MibTableColumn((1, 3, 6, 1, 3, 123, 2, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0,64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrMODescr.setDescription('A textual description of the object that will\n            be aggregated.')
aggrMOEntryStorageType = MibTableColumn((1, 3, 6, 1, 3, 123, 2, 1, 5), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrMOEntryStorageType.setDescription("This object defines whether the parameters defined in\n            this row are kept in volatile storage and lost upon\n            reboot or backed up by non-volatile (permanent)\n            storage.\n            Conceptual rows having the value 'permanent' need not\n            allow write-access to any columnar objects in the row.\n           ")
aggrMOEntryStatus = MibTableColumn((1, 3, 6, 1, 3, 123, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrMOEntryStatus.setDescription("The row status variable, used according to row\n            installation and removal conventions.\n            Objects in a row can be modified only when the value of\n            this object in the corresponding conceptual row is not\n            'active'.\n            Thus, to modify one or more of the objects in this\n            conceptual row,\n              a. change the row status to 'notInService',\n              b. change the values of the row, and\n              c. change the row status to 'active'.\n            The aggrMOEntryStatus may be changed to 'active' iff\n            all the MOs in the conceptual row have been assigned\n            valid values.\n           ")
aggrDataTable = MibTable((1, 3, 6, 1, 3, 123, 3), )
if mibBuilder.loadTexts: aggrDataTable.setDescription('Each row of this table contains information\n            about an aggregateMO indexed by aggrCtlEntryID.')
aggrDataEntry = MibTableRow((1, 3, 6, 1, 3, 123, 3, 1), ).setIndexNames((0, "AGGREGATE-MIB", "aggrCtlEntryID"))
if mibBuilder.loadTexts: aggrDataEntry.setDescription('Entry containing information pertaining to\n            an aggregate MO.')
aggrDataRecord = MibTableColumn((1, 3, 6, 1, 3, 123, 3, 1, 1), AggrMOValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrDataRecord.setDescription('The snapshot value of the aggregated MO.\n           Note that the access privileges to this object will be\n           governed by the access privileges of the component\n           objects.  Thus, an entity attempting to access an\n           instance of this MO MUST have access rights to all the\n           component instance objects and this MO instance.\n          ')
aggrDataRecordCompressed = MibTableColumn((1, 3, 6, 1, 3, 123, 3, 1, 2), AggrMOCompressedValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrDataRecordCompressed.setDescription("The compressed value of the aggregated MO.\n           The compression algorithm will depend on the\n           aggrCtlCompressionAlgorithm given in the corresponding\n           aggrCtlEntry.  If the value of the corresponding\n           aggrCtlCompressionAlgorithm is (1) 'none', then the value\n           of all instances of this object will be a string of zero\n           length.\n           Note that the access privileges to this object will be\n           governed by the access privileges of the component\n           objects.  Thus, an entity attempting to access an instance\n           of this MO MUST have access rights to all the component\n           instance objects and this MO instance.\n          ")
aggrDataErrorRecord = MibTableColumn((1, 3, 6, 1, 3, 123, 3, 1, 3), AggrMOErrorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrDataErrorRecord.setDescription('The error status corresponding to the MO instances\n            aggregated in aggrDataRecord (and\n            aggrDataRecordCompressed).')
aggrConformance = MibIdentifier((1, 3, 6, 1, 3, 123, 4))
aggrGroups = MibIdentifier((1, 3, 6, 1, 3, 123, 4, 1))
aggrCompliances = MibIdentifier((1, 3, 6, 1, 3, 123, 4, 2))
aggrMibCompliance = ModuleCompliance((1, 3, 6, 1, 3, 123, 4, 2, 1)).setObjects(*(("AGGREGATE-MIB", "aggrMibBasicGroup"),))
if mibBuilder.loadTexts: aggrMibCompliance.setDescription('The compliance statement for SNMP entities\n                 that implement the AGGREGATE-MIB.')
aggrMibBasicGroup = ObjectGroup((1, 3, 6, 1, 3, 123, 4, 1, 1)).setObjects(*(("AGGREGATE-MIB", "aggrCtlMOIndex"), ("AGGREGATE-MIB", "aggrCtlMODescr"), ("AGGREGATE-MIB", "aggrCtlCompressionAlgorithm"), ("AGGREGATE-MIB", "aggrCtlEntryOwner"), ("AGGREGATE-MIB", "aggrCtlEntryStorageType"), ("AGGREGATE-MIB", "aggrCtlEntryStatus"), ("AGGREGATE-MIB", "aggrMOInstance"), ("AGGREGATE-MIB", "aggrMODescr"), ("AGGREGATE-MIB", "aggrMOEntryStorageType"), ("AGGREGATE-MIB", "aggrMOEntryStatus"), ("AGGREGATE-MIB", "aggrDataRecord"), ("AGGREGATE-MIB", "aggrDataRecordCompressed"), ("AGGREGATE-MIB", "aggrDataErrorRecord"),))
if mibBuilder.loadTexts: aggrMibBasicGroup.setDescription('A collection of objects for aggregation of MOs.')
mibBuilder.exportSymbols("AGGREGATE-MIB", aggrCtlMODescr=aggrCtlMODescr, aggrMOInstance=aggrMOInstance, PYSNMP_MODULE_ID=aggrMIB, aggrMOEntry=aggrMOEntry, aggrGroups=aggrGroups, aggrMOEntryStorageType=aggrMOEntryStorageType, aggrCompliances=aggrCompliances, aggrCtlEntryStorageType=aggrCtlEntryStorageType, aggrMODescr=aggrMODescr, aggrCtlCompressionAlgorithm=aggrCtlCompressionAlgorithm, aggrDataRecord=aggrDataRecord, aggrCtlEntryOwner=aggrCtlEntryOwner, aggrDataErrorRecord=aggrDataErrorRecord, aggrMibBasicGroup=aggrMibBasicGroup, aggrDataEntry=aggrDataEntry, AggrMOErrorStatus=AggrMOErrorStatus, aggrMOEntryStatus=aggrMOEntryStatus, aggrMIB=aggrMIB, aggrMOTable=aggrMOTable, aggrCtlEntry=aggrCtlEntry, AggrMOValue=AggrMOValue, aggrCtlEntryStatus=aggrCtlEntryStatus, aggrCtlMOIndex=aggrCtlMOIndex, aggrMOEntryMOID=aggrMOEntryMOID, AggrMOCompressedValue=AggrMOCompressedValue, aggrCtlEntryID=aggrCtlEntryID, aggrConformance=aggrConformance, aggrMOEntryID=aggrMOEntryID, aggrCtlTable=aggrCtlTable, aggrDataRecordCompressed=aggrDataRecordCompressed, aggrDataTable=aggrDataTable, aggrMibCompliance=aggrMibCompliance)
