/**
 * Autogenerated by Thrift Compiler (0.7.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 */
package elephantdb.generated;

import org.apache.commons.lang.builder.HashCodeBuilder;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.EnumMap;
import java.util.Set;
import java.util.HashSet;
import java.util.EnumSet;
import java.util.Collections;
import java.util.BitSet;
import java.nio.ByteBuffer;
import java.util.Arrays;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ElephantDBSearch {

  public interface Iface extends ElephantDBShared.Iface {

  }

  public interface AsyncIface extends ElephantDBShared .AsyncIface {

  }

  public static class Client extends ElephantDBShared.Client implements Iface {
    public static class Factory implements org.apache.thrift7.TServiceClientFactory<Client> {
      public Factory() {}
      public Client getClient(org.apache.thrift7.protocol.TProtocol prot) {
        return new Client(prot);
      }
      public Client getClient(org.apache.thrift7.protocol.TProtocol iprot, org.apache.thrift7.protocol.TProtocol oprot) {
        return new Client(iprot, oprot);
      }
    }

    public Client(org.apache.thrift7.protocol.TProtocol prot)
    {
      super(prot, prot);
    }

    public Client(org.apache.thrift7.protocol.TProtocol iprot, org.apache.thrift7.protocol.TProtocol oprot) {
      super(iprot, oprot);
    }

  }
  public static class AsyncClient extends ElephantDBShared.AsyncClient implements AsyncIface {
    public static class Factory implements org.apache.thrift7.async.TAsyncClientFactory<AsyncClient> {
      private org.apache.thrift7.async.TAsyncClientManager clientManager;
      private org.apache.thrift7.protocol.TProtocolFactory protocolFactory;
      public Factory(org.apache.thrift7.async.TAsyncClientManager clientManager, org.apache.thrift7.protocol.TProtocolFactory protocolFactory) {
        this.clientManager = clientManager;
        this.protocolFactory = protocolFactory;
      }
      public AsyncClient getAsyncClient(org.apache.thrift7.transport.TNonblockingTransport transport) {
        return new AsyncClient(protocolFactory, clientManager, transport);
      }
    }

    public AsyncClient(org.apache.thrift7.protocol.TProtocolFactory protocolFactory, org.apache.thrift7.async.TAsyncClientManager clientManager, org.apache.thrift7.transport.TNonblockingTransport transport) {
      super(protocolFactory, clientManager, transport);
    }

  }

  public static class Processor<I extends Iface> extends ElephantDBShared.Processor implements org.apache.thrift7.TProcessor {
    private static final Logger LOGGER = LoggerFactory.getLogger(Processor.class.getName());
    public Processor(I iface) {
      super(iface, getProcessMap(new HashMap<String, org.apache.thrift7.ProcessFunction<I, ? extends org.apache.thrift7.TBase>>()));
    }

    protected Processor(I iface, Map<String,  org.apache.thrift7.ProcessFunction<I, ? extends  org.apache.thrift7.TBase>> processMap) {
      super(iface, getProcessMap(processMap));
    }

    private static <I extends Iface> Map<String,  org.apache.thrift7.ProcessFunction<I, ? extends  org.apache.thrift7.TBase>> getProcessMap(Map<String,  org.apache.thrift7.ProcessFunction<I, ? extends  org.apache.thrift7.TBase>> processMap) {
      return processMap;
    }

  }

}
