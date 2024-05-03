import logging
import os

log = logging.getLogger(__name__)
log.setLevel(level=logging.INFO)
logging.basicConfig(level=logging.INFO)
package_dir = os.path.dirname(os.path.abspath(__file__))

__all__ = ['log', 'package_dir']
