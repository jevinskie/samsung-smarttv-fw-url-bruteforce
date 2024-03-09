import logging
import typing
from functools import cached_property

import requests

from .url_bundle import URLBundle

log = logging.getLogger("samsung-smarttv-fw-url-bruteforce:url_checker")


class URLChecker:
    def url_is_live(self, url: str) -> bool:
        try:
            resp = self.session.head(url)
        except requests.RequestException as e:
            log.exception(f"Got exception requesting HEAD on {url}.", exc_info=e)
            return False
        requests.status_codes.codes.ok = typing.cast(
            int, requests.status_codes.codes.ok
        )
        return resp.status_code == requests.status_codes.codes.ok

    @cached_property
    def session(self) -> requests.Session:
        return requests.Session()


def get_live_urls(url_bundles: tuple[URLBundle, ...]) -> tuple[URLBundle, ...]:
    chk = URLChecker()
    live_urls: list[URLBundle] = []
    for bndl in url_bundles:
        live: bool = chk.url_is_live(bndl.url)
        if live:
            bndl.live = live
            live_urls.append(bndl)
    return tuple(live_urls)
