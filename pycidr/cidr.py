from netaddr import *
try: 
    import cPickle as pickle
except: 
    import pickle

class CIDR:
    """ Allows CIDRs to be labeled, and queried.
    """
    def __init__(self):
        self.d = {}

    def _get_key_list(self, cidr):
        """ Produces a list of keys by which the value will be referenced. 
            We always just use the first octet, and then we include bits up
            to the length of the mask in the CIDR.
        """ 

        # Determine IP Bits
        ipn = IPNetwork(cidr)
        bits = "".join(ipn.network.bits().split("."))[8:]

        # First Octet
        o = cidr.split(".")[0]

        if "/" in cidr:
            # Remaining Bits in Mask
            mask = int(cidr.split("/")[-1])-8

        else:
            mask = 24

        # Total Key List
        return [o]+list(bits[:mask])

    def _find(self, bits):
        """ Find the leaf node based on a list of keys. 
            We give preference to larger CIDRs, so if at any time a non-dict
            is encountered, this is returned.
        """

        # Locate First Specified CIDR or return dict
        d = self.d
        for k in bits[:-1]:
            if not k in d:
                d[k] = {}
            d = d[k]
            if not type(d)==dict: break
        return d

    def __setitem__(self, cidr, value):
        """ Assign value to CIDR if it is not already contained in larger CIDR.
        """
        bits = self._get_key_list(cidr)

        d = self._find(bits)
        if type(d)==dict:
            d[bits[-1]] = value

    def __getitem__(self, cidr):       
        """ Return largest CIDR value that contains specified CIDR.
        """

        bits = self._get_key_list(cidr)
        d = self._find(bits)
        if type(d)==dict: raise KeyError("CIDR %s Not Specified"%(cidr,))
        return d

    def save(self, fname):
        """ Dump to Pickle Object
        """
        f = open(fname,'w')
        pickle.dump(self.d, f)
        f.close()

    def load(self, fname):
        f = open(fname,'r')
        self.d = pickle.load(f)
        f.close()

