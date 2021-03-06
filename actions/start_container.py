from lib.actions import BaseAction

__all__ = [
    'StartContainerAction'
]


class StartContainerAction(BaseAction):
    api_type = 'container'

    def run(self, credentials, container_id, extra_kwargs=None):
        extra_kwargs = extra_kwargs or {}
        driver = self._get_driver_for_credentials(credentials=credentials)
        container = driver.get_container(container_id)

        self.logger.info('Starting container: %s' % (container))
        status = container.start(**extra_kwargs)

        if status is True:
            self.logger.info('Successfully started container "%s"' % (container))
        else:
            self.logger.error('Failed to start container "%s"' % (container))

        return status
