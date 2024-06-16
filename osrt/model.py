from torch import nn

from osrt.encoder import OSRTEncoder, ImprovedSRTEncoder, OSRTEncoderDynSlots, OSRTEncoderAttentionDynSlots
from osrt.decoder import SlotMixerDecoder, SpatialBroadcastDecoder, ImprovedSRTDecoder, SlotMixerDecoderDynSlots

import osrt.layers as layers

class OSRT(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        encoder_type = cfg['encoder']
        decoder_type = cfg['decoder']

        layers.__USE_DEFAULT_INIT__ = cfg.get('use_default_init', False)

        if encoder_type == 'srt':
            self.encoder = ImprovedSRTEncoder(**cfg['encoder_kwargs'])
        elif encoder_type == 'osrt':
            self.encoder = OSRTEncoder(**cfg['encoder_kwargs'])
        elif encoder_type == "osrt_dyn":
            self.encoder = OSRTEncoderDynSlots(**cfg['encoder_kwargs'])
        elif encoder_type == "osrt_dyn_attn":
            self.encoder = OSRTEncoderAttentionDynSlots(**cfg['encoder_kwargs'])
        else:
            raise ValueError(f'Unknown encoder type: {encoder_type}')


        if decoder_type == 'spatial_broadcast':
            self.decoder = SpatialBroadcastDecoder(**cfg['decoder_kwargs'])
        elif decoder_type == 'srt':
            self.decoder = ImprovedSRTDecoder(**cfg['decoder_kwargs'])
        elif decoder_type == 'slot_mixer':
            self.decoder = SlotMixerDecoder(**cfg['decoder_kwargs'])
        elif decoder_type == 'slot_mixer_dyn':
            self.decoder = SlotMixerDecoderDynSlots(**cfg['decoder_kwargs'])
        else:
            raise ValueError(f'Unknown decoder type: {decoder_type}')


