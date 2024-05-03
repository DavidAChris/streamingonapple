import csv
import io
from datetime import datetime
from appleparser import log


class State:
    def __init__(self, **kwargs):
        log.info("Init State")
        self.__new_assets: list[dict] = []
        self.__current_assets: list[dict] = []
        self.__asset_keys = set()

    def is_unique_asset(self, file_key: str) -> bool:
        """Check if the asset has been collected already"""
        is_unique = bool(file_key not in self.__asset_keys)
        if is_unique:
            self.__asset_keys.add(file_key)
        return is_unique

    def add_current_asset(self, asset: dict):
        if asset and asset not in self.__current_assets:
            self.__current_assets.append(asset)

    def get_current_assets(self):
        return self.__current_assets

    def add_new_asset(self, asset: dict):
        """Add a new asset to the providers data"""
        self.__new_assets.append(asset)

    def get_new_assets(self):
        return self.__new_assets

    def format_csv(self) -> bytes:
        with io.StringIO() as buf:
            if not self.__new_assets:
                return b''
            field_names = self.__new_assets[0].keys()
            writer = csv.DictWriter(buf, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(self.__new_assets)
            body = buf.getvalue().encode('UTF-8')
            return body

    def future_date_eval(self, date: datetime) -> bool:
        """Evaluate if the provided time is a future date or not"""
        return (date and not date > datetime.now()) or not date
