import json

class ObjetJson:
    def to_json(self) -> str:
        """[to_json]
            convert object to a json
        """
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)