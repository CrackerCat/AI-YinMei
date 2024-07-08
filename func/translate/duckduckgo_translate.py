from duckduckgo_search import DDGS
from func.config.default_config import defaultConfig
from func.log.default_log import DefaultLog
from func.tools.singleton_mode import singleton

@singleton
class DuckduckgoTranslate:
    # 设置控制台日志
    log = DefaultLog().getLogger()
    # 加载配置
    config = defaultConfig().get_config()
    duckduckgo_proxies = config["proxies"]["DuckduckgoProxies"]

    def __init__(self):
        pass

    # 翻译
    def translate(self, text, from_lanuage, to_lanuage):
        with DDGS(proxies=self.duckduckgo_proxies, timeout=20) as ddgs:
            try:
                r = ddgs.translate(text, from_=from_lanuage, to=to_lanuage)
                self.log.info(f"翻译：{r}")
                return r
            except Exception as e:
                self.log.exception(f"translate信息回复异常{e}")
            return text
