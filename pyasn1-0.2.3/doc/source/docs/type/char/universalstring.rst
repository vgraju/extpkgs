
.. |ASN.1| replace:: UniversalString

.. |encoding| replace:: utf-32-be

|ASN.1| type
------------

.. autoclass:: pyasn1.type.char.UniversalString(value=NoValue(), tagSet=TagSet(), subtypeSpec=ConstraintsIntersection(), encoding='us-ascii')
   :members: hasValue, isSameTypeWith, isSuperTypeOf, tagSet

   .. note::

       The |ASN.1| type models a Unicode (ISO10646-1) character string implicitly serialized into UTF-32 big endian.

   .. automethod:: pyasn1.type.char.UniversalString.clone(value=NoValue(), tagSet=TagSet(), subtypeSpec=ConstraintsIntersection(), encoding='us-ascii')
   .. automethod:: pyasn1.type.char.UniversalString.subtype(value=NoValue(), implicitTag=Tag(), explicitTag=Tag(),subtypeSpec=ConstraintsIntersection(), encoding='us-ascii')
