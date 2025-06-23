import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.const import (
  CONF_CS_PIN, CONF_DC_PIN, CONF_BUSY_PIN,
  CONF_RESET_PIN, CONF_CLK_PIN, CONF_MOSI_PIN,
)
from esphome.components import display
from esphome import pins

# Create namespace and class
gxepd2_ns = cg.esphome_ns.namespace('gxepd2_display')
GxEPD2Display = gxepd2_ns.class_(
  'GxEPD2Display', cg.Component, display.DisplayBuffer)

# Define config schema for the platform under display:
CONFIG_SCHEMA = display.BASIC_DISPLAY_SCHEMA.extend({
  cv.GenerateID(): cv.declare_id(GxEPD2Display),
  cv.Required(CONF_CS_PIN): pins.gpio_output_pin_schema,
  cv.Required(CONF_DC_PIN): pins.gpio_output_pin_schema,
  cv.Required(CONF_BUSY_PIN): pins.gpio_input_pin_schema,
  cv.Required(CONF_RESET_PIN): pins.gpio_output_pin_schema,
  cv.Required(CONF_MOSI_PIN): pins.gpio_output_pin_schema,
  cv.Required(CONF_CLK_PIN): pins.gpio_output_pin_schema,
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(
        config[CONF_ID],
        config[CONF_CS_PIN],
        config[CONF_DC_PIN],
        config[CONF_BUSY_PIN],
        config[CONF_RESET_PIN],
        config[CONF_MOSI_PIN],
        config[CONF_CLK_PIN],
    )
    await cg.register_component(var, config)
    display.setup_display(var, config)
    cg.add_library(
        name='GxEPD2',
        repository='https://github.com/ZinggJM/GxEPD2.git',
        version='1.5.3'
    )
