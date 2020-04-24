# used for storing template strings for pybind functionalities

from string import Template

# module
#######################################################################################

# requires: $MODULE_NAME, $DOCSTRING
string_module_define=Template(
	'PYBIND11_MODULE($MODULE_NAME, m) {
    m.doc() = "$DOCSTRING"; // module docstring'
)

# requires: nothing
string_module_end=Template(
	'}'
)

# class
#######################################################################################

# requires: $CLASS_NAME
string_class_define=Template(
	'py::class_<$CLASS_NAME>(m, "$CLASS_NAME")'
)

# requires: nothing
string_class_end=Template(
	';'
)

# requires: $CLASS_CONSTRUCTOR_ARGUMENTS
# remove reference name, check later
string_class_constructor=Template(
	'.def(py::init<$CLASS_CONSTRUCTOR_ARGUMENTS>())'
)

# requires: $CLASS_NAME, $CLASS_REPRESENTATION_MESSAGE
string_class_representation=Template(
	'.def("__repr__",
        [](const $CLASS_NAME &a) {
            return "<$CLASS_NAME: $CLASS_REPRESENTATION_MESSAGE>";
        }'
)

# requires: $CLASS_NAME, $CLASS_FIELD
string_class_expose_rw=Template(
	'.def_readwrite("$CLASS_FIELD", &$CLASS_NAME::$CLASS_FIELD)'
)

# requires: $CLASS_NAME, $CLASS_FIELD
string_class_expose_ronly=Template(
	'.def_readonly("$CLASS_FIELD", &$CLASS_NAME::$CLASS_FIELD)'
)

# requires: $CLASS_NAME, $CLASS_FIELD, $GETTER, $SETTER
string_class_property_getset=Template(
	'.def_property("$CLASS_FIELD", &$CLASS_NAME::$GETTER, &Pet::$SETTER)'
)

# requires: $CLASS_NAME, $CLASS_FIELD, $GETTER
string_class_property_get=Template(
	'.def_property("$CLASS_FIELD", &$CLASS_NAME::$GETTER)'
)

# requires: $CLASS_NAME, $CLASS_FIELD, $SETTER
string_class_property_set=Template(
	'.def_property("$CLASS_FIELD", &$CLASS_NAME::nullptr, &Pet::$SETTER)'


# function
#######################################################################################

# requires: $FUNCTION_NAME, $DOCSTRING
string_function_define=Template(
	'm.def("$FUNCTION_NAME", &$FUNCTION_NAME, "$DOCSTRING"'
)

# requires: nothing
string_function_end=Template(
	');'
)

# requires: $FUNCTION_ARGUMENT
string_function_arguments=Template(
	', py::arg("$FUNCTION_ARGUMENT")'
)

#######################################################################################

# requires: $VARIABLE_NAME, $VARIABLE_VALUE
string_export_variable=Template(
	'm.attr("$VARIABLE_NAME") = $VARIABLE_VALUE;'
)

# requires: $CAST_FROM, $CAST_TO
# check this later
string cast_explicit_variable=Template(
	'py::object $CAST_FROM = py::cast("$CAST_FROM");'
)