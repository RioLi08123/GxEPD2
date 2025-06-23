import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.const import CONF_ID, CONF_CS_PIN, CONF_DC_PIN, CONF_BUSY_PIN, CONF_RESET_PIN, CONF_MOSI_PIN, CONF_CLK_PIN

gxepd2_ns = cg.esphome_ns.namespace('gxepd2_display')
GxEPD2Display = gxepd2_ns.class_('GxEPD2Display', cg.Component, cg.DisplayBuffer)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(GxEPD2Display),
    cv.Required(CONF_CS_PIN): cv.pin,
    cv.Required(CONF_DC_PIN): cv.pin,
    cv.Required(CONF_BUSY_PIN): cv.pin,
    cv.Required(CONF_RESET_PIN): cv.pin,
    cv.Required(CONF_MOSI_PIN): cv.pin,
    cv.Required(CONF_CLK_PIN): cv.pin,
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID],
                           config[CONF_CS_PIN], config[CONF_DC_PIN],
                           config[CONF_BUSY_PIN], config[CONF_RESET_PIN],
                           config[CONF_MOSI_PIN], config[CONF_CLK_PIN])
    await cg.register_component(var, config)
    cg.add_library(
        name='GxEPD2',
        repository='https://github.com/ZinggJM/GxEPD2.git',
        version='1.5.3'
    )
    return var
