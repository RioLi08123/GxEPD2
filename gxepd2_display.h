#pragma once
#include "esphome.h"
#include <GxEPD2_BW.h>

class GxEPD2Display : public Component, public DisplayBuffer {
 public:
  GxEPD2Display(int cs, int dc, int busy, int rst, int mosi, int clk);

  void setup() override;
  void dump_config() override;
  void update() override;
  void display() override;

 protected:
  int cs_, dc_, busy_, rst_, mosi_, clk_;
  GxEPD2_BW<GxEPD2_4G_BW, GxEPD2_4G_BW::HEIGHT> *disp_;  // adjust template to 4.26"
};
