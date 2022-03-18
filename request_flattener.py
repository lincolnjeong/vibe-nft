class RequestBodyFlattener:

    def __flatten_key_value(self, key, value):
        if (isinstance(value, str)):
            return f"{key}={value}"

        if (isinstance(value, list)):
            l_key_value = {}
            for index, ele in enumerate(value):
                for lkey in list(ele.keys() | l_key_value.keys()):
                    if lkey in ele.keys():
                        lvalue = ele[lkey]
                    else:
                        lvalue = ""

                    if (lkey in l_key_value.keys()):
                        l_key_value[lkey] = f"{l_key_value[lkey]},{lvalue}"
                    else:
                        l_key_value[lkey] = f"{',' * index}{lvalue}"
            return "&".join("%s=%s" % (f"{key}.{lkey}", lvalue) for (lkey, lvalue) in sorted(l_key_value.items()))

    def flatten(self, body: dict = {}):
        sorted_body = sorted(body.items())
        return "&".join(self.__flatten_key_value(key, value) for (key, value) in sorted_body)