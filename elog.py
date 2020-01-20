import logging

logging.basicConfig(level=logging.INFO, format='%(asctime1)s %(levelname)s %(message)s')


logger = logging.getLogger(__name__)

logger.info("Start print log")


logger.warning("Something maybe fail.")