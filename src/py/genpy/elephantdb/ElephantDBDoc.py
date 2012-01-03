#
# Autogenerated by Thrift Compiler (0.7.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

from thrift.Thrift import *
import elephantdb.ElephantDBShared
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface(elephantdb.ElephantDBShared.Iface):
  def get(self, domain, key):
    """
    Parameters:
     - domain
     - key
    """
    pass

  def getField(self, domain, key, field):
    """
    Parameters:
     - domain
     - key
     - field
    """
    pass

  def getFields(self, domain, key, fields):
    """
    Parameters:
     - domain
     - key
     - fields
    """
    pass


class Client(elephantdb.ElephantDBShared.Client, Iface):
  def __init__(self, iprot, oprot=None):
    elephantdb.ElephantDBShared.Client.__init__(self, iprot, oprot)

  def get(self, domain, key):
    """
    Parameters:
     - domain
     - key
    """
    self.send_get(domain, key)
    return self.recv_get()

  def send_get(self, domain, key):
    self._oprot.writeMessageBegin('get', TMessageType.CALL, self._seqid)
    args = get_args()
    args.domain = domain
    args.key = key
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_get(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = get_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "get failed: unknown result");

  def getField(self, domain, key, field):
    """
    Parameters:
     - domain
     - key
     - field
    """
    self.send_getField(domain, key, field)
    return self.recv_getField()

  def send_getField(self, domain, key, field):
    self._oprot.writeMessageBegin('getField', TMessageType.CALL, self._seqid)
    args = getField_args()
    args.domain = domain
    args.key = key
    args.field = field
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_getField(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = getField_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "getField failed: unknown result");

  def getFields(self, domain, key, fields):
    """
    Parameters:
     - domain
     - key
     - fields
    """
    self.send_getFields(domain, key, fields)
    return self.recv_getFields()

  def send_getFields(self, domain, key, fields):
    self._oprot.writeMessageBegin('getFields', TMessageType.CALL, self._seqid)
    args = getFields_args()
    args.domain = domain
    args.key = key
    args.fields = fields
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_getFields(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = getFields_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "getFields failed: unknown result");


class Processor(elephantdb.ElephantDBShared.Processor, Iface, TProcessor):
  def __init__(self, handler):
    elephantdb.ElephantDBShared.Processor.__init__(self, handler)
    self._processMap["get"] = Processor.process_get
    self._processMap["getField"] = Processor.process_getField
    self._processMap["getFields"] = Processor.process_getFields

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_get(self, seqid, iprot, oprot):
    args = get_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = get_result()
    result.success = self._handler.get(args.domain, args.key)
    oprot.writeMessageBegin("get", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_getField(self, seqid, iprot, oprot):
    args = getField_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = getField_result()
    result.success = self._handler.getField(args.domain, args.key, args.field)
    oprot.writeMessageBegin("getField", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_getFields(self, seqid, iprot, oprot):
    args = getFields_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = getFields_result()
    result.success = self._handler.getFields(args.domain, args.key, args.fields)
    oprot.writeMessageBegin("getFields", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class get_args:
  """
  Attributes:
   - domain
   - key
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'domain', None, None, ), # 1
    (2, TType.STRING, 'key', None, None, ), # 2
  )

  def __init__(self, domain=None, key=None,):
    self.domain = domain
    self.key = key

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.domain = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.key = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('get_args')
    if self.domain is not None:
      oprot.writeFieldBegin('domain', TType.STRING, 1)
      oprot.writeString(self.domain.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.key is not None:
      oprot.writeFieldBegin('key', TType.STRING, 2)
      oprot.writeString(self.key.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class get_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (Value, Value.thrift_spec), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = Value()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('get_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getField_args:
  """
  Attributes:
   - domain
   - key
   - field
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'domain', None, None, ), # 1
    (2, TType.STRING, 'key', None, None, ), # 2
    (3, TType.STRING, 'field', None, None, ), # 3
  )

  def __init__(self, domain=None, key=None, field=None,):
    self.domain = domain
    self.key = key
    self.field = field

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.domain = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.key = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.field = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getField_args')
    if self.domain is not None:
      oprot.writeFieldBegin('domain', TType.STRING, 1)
      oprot.writeString(self.domain.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.key is not None:
      oprot.writeFieldBegin('key', TType.STRING, 2)
      oprot.writeString(self.key.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.field is not None:
      oprot.writeFieldBegin('field', TType.STRING, 3)
      oprot.writeString(self.field.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getField_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (Value, Value.thrift_spec), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = Value()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getField_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getFields_args:
  """
  Attributes:
   - domain
   - key
   - fields
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'domain', None, None, ), # 1
    (2, TType.STRING, 'key', None, None, ), # 2
    (3, TType.LIST, 'fields', (TType.STRING,None), None, ), # 3
  )

  def __init__(self, domain=None, key=None, fields=None,):
    self.domain = domain
    self.key = key
    self.fields = fields

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.domain = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.key = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.fields = []
          (_etype173, _size170) = iprot.readListBegin()
          for _i174 in xrange(_size170):
            _elem175 = iprot.readString().decode('utf-8')
            self.fields.append(_elem175)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getFields_args')
    if self.domain is not None:
      oprot.writeFieldBegin('domain', TType.STRING, 1)
      oprot.writeString(self.domain.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.key is not None:
      oprot.writeFieldBegin('key', TType.STRING, 2)
      oprot.writeString(self.key.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.fields is not None:
      oprot.writeFieldBegin('fields', TType.LIST, 3)
      oprot.writeListBegin(TType.STRING, len(self.fields))
      for iter176 in self.fields:
        oprot.writeString(iter176.encode('utf-8'))
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getFields_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (Value, Value.thrift_spec), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = Value()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getFields_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
