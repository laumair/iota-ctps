class transaction:
    def __init__(self,tryte_string, hash_string):
        self.hash = hash_string
        #self.signature_message_fragment = tryte_string[0:2187]
        self.address = tryte_string[2187:2268]
        self.value = tryte_string[2268:2295]
        self.tag = tryte_string[2295:2322]
        self.timestamp = tryte_string[2322:2331]
        #self.current_index = tryte_string[2331:2340]
        #self.last_index = tryte_string[2340:2349]
        self.bundle_hash = tryte_string[2349:2430]
        self.trunk_transaction_hash = tryte_string[2430:2511]
        self.branch_transaction_hash = tryte_string[2511:2592]
        #self.nonce = tryte_string[2592:2673]
