#include "gxepd2_display.h"
#include "esphome/core/log.h"

static const char *TAG = "gxepd2_display";

GxEPD2Display::GxEPD2Display(int cs, int dc, int busy, int rst, int mosi, int clk)
  : cs_(cs), dc_(dc), busy_(busy), rst_(rst), mosi_(mosi), clk_(clk) {}

void GxEPD2Display::setup() {
  ESP_LOGCONFIG(TAG, "Setting up GxEPD2 display...");
  disp_ = new GxEPD2_BW<GxEPD2_4G_BW, GxEPD2_4G_BW::HEIGHT>(
    cs_, dc_, rst_, busy_);
  disp_->spiSettings = SPISettings(2000000, MSBFIRST, SPI_MODE0);
  disp_->init(0);
  disp_->setRotation(1);
}

void GxEPD2Display::dump_config() {
  ESP_LOGCONFIG(TAG, "GxEPD2 CS=%d DC=%d BUSY=%d RST=%d MOSI=%d CLK=%d",
                cs_, dc_, busy_, rst_, mosi_, clk_);
}

void GxEPD2Display::update() {
  if (this->has_buffer()) {
    disp_->firstPage();
    do {
      display();  // call display() to draw buffer
    } while (disp_->nextPage());
  }
}

void GxEPD2Display::display() {
  auto it = this->get_buffer();
  disp_->drawBuffer(0, 0, this->get_width(), this->get_height(),
                    it->buffer.data(), it->bytes_per_row);
}
