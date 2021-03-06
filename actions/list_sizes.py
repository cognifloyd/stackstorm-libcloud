from lib.actions import BaseAction

__all__ = [
    'ListSizesAction'
]


class ListSizesAction(BaseAction):
    api_type = 'compute'

    def run(self, credentials, extra_kwargs=None):
        extra_kwargs = extra_kwargs or {}
        driver = self._get_driver_for_credentials(credentials=credentials)
        sizes = driver.list_sizes()
        return self.resultsets.formatter(sizes)
