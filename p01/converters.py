# 自定义路由转换器

# 自定义之后需要在总路由注册路由转换器



class MobileConverter:
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)












