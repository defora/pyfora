from abc import ABCMeta

class Datastream(metaclass=ABCMeta):
	class ControlGroup(Enum):
		REDIRECT = auto()
		EXTERNAL = auto()
		MANAGED = auto()
		INLINE = auto()
	@abstractproperty
	def ds_control_group:
		return NotImplemented
	@abstractproperty
	def ds_info_type:
		return NotImplemented
	@abstractproperty
	def ds_state:
		return NotImplemented
	@abstractproperty
	def ds_versionable:
		return NotImplemented
