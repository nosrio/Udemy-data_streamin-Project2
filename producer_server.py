from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    #TODO we're generating a dummy data
    #def generate_data(self):
    #    with open(self.input_file) as f:
    #        for line in f:
    #            message = self.dict_to_binary(line)
    #            # TODO send the correct data
    #            self.send(self.topic,message)
    #            time.sleep(1)
    # Had to write a new 'generate_data' function because previous function was sending only string lines to kafka instead of json .
    def generate_data(self):
        with open(self.input_file) as f:
            json_info = json.load(f)
        
        for info in json_info:
            message = self.dict_to_binary(info)
            self.send(self.topic,message)
            time.sleep(1)
    
    # TODO fill this in to return the json dictionary to binary
    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode('utf-8')
        