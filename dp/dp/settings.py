# -*- coding: utf-8 -*-

# Scrapy settings for dp project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dp'

SPIDER_MODULES = ['dp.spiders']
NEWSPIDER_MODULE = 'dp.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dp (+http://www.yourdomain.com)'
#USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
REDIRECT_ENABLED = False
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
COOKIES_DEBUG = True
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Host': 'www.dianping.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Connection': 'keep-alive',
}

COOKIE = {'showNav': '#nav-tab|0|1', 'navCtgScroll': '0', '_lxsdk_cuid': '164b0658837c8-0ea560583c0c68-6b1b1279-1fa400-164b065883762', '_lxsdk': '164b0658837c8-0ea560583c0c68-6b1b1279-1fa400-164b065883762', '_hc.v': '7b174aa1-e83d-1c28-5eb3-d4a656dae863.1531967802', '__utma': '205923334.1273454000.1531968483.1531968483.1531968483.1', '__utmz': '205923334.1531968483.1.1.utmcsr', 'ctu': '383b4eeb970a809dd2f534730b186b40e6ab09579b4b72d0531260ca8b2ba56a', '_dp.ac.v': '850504c6-288c-4add-9731-7c00087fc61d', '_lx_utm': 'utm_source%3DBaidu%26utm_medium%3Dorganic', 'lgtoken': '0b0b7c714-9956-4708-8b6d-ba9e269f84ad', 'dper': 'a51fe1be04311badcb3fb5d4a6b08996cac520b1f2f812cdc2d41927672c0d0600489a61c0896ef000445497aec6cc2dc6b3fac20aaab05b3bc01526e3904756f22050712a0b26995edbffe2ef61311b525377a17ca75dc243d8ddce20c447ae', 'll': '7fd06e815b796be3df069dec7836c3df', 'ua': 'mInQ_532', 'cy': '1', 'cye': 'shanghai', 's_ViewType': '10', '_lxsdk_s': '164d524f87f-64d-33-b2e%7C%7C245'}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'dp.middlewares.DpSpiderMiddleware': 543,
#}
# HTTPERROR_ALLOWED_CODES = [407]
# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'dp.middlewares.MyproxiesSpiderMiddleware': 200,
#    'dp.middlewares.DpDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'dp.pipelines.DpPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
