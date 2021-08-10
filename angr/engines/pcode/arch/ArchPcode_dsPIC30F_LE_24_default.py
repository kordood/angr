###
### This file was automatically generated
###

from archinfo.arch import register_arch, Endness, Register

from .common import ArchPcode


class ArchPcode_dsPIC30F_LE_24_default(ArchPcode):
    name = 'dsPIC30F:LE:24:default'
    pcode_arch = 'dsPIC30F:LE:24:default'
    description = 'dsPIC30F'
    bits = 24
    ip_offset = 0x2e
    sp_offset = 0x1e
    bp_offset = sp_offset
    instruction_endness = Endness.LE
    register_list = [
        Register('w1w0', 4, 0x0),
        Register('w0', 2, 0x0),
        Register('w0byte', 1, 0x0),
        Register('w1', 2, 0x2),
        Register('w1byte', 1, 0x2),
        Register('w3w2', 4, 0x4),
        Register('w2', 2, 0x4),
        Register('w2byte', 1, 0x4),
        Register('w3', 2, 0x6),
        Register('w3byte', 1, 0x6),
        Register('w5w4', 4, 0x8),
        Register('w4', 2, 0x8),
        Register('w4byte', 1, 0x8),
        Register('w5', 2, 0xa),
        Register('w5byte', 1, 0xa),
        Register('w7w6', 4, 0xc),
        Register('w6', 2, 0xc),
        Register('w6byte', 1, 0xc),
        Register('w7', 2, 0xe),
        Register('w7byte', 1, 0xe),
        Register('w9w8', 4, 0x10),
        Register('w8', 2, 0x10),
        Register('w8byte', 1, 0x10),
        Register('w9', 2, 0x12),
        Register('w9byte', 1, 0x12),
        Register('w11w10', 4, 0x14),
        Register('w10', 2, 0x14),
        Register('w10byte', 1, 0x14),
        Register('w11', 2, 0x16),
        Register('w11byte', 1, 0x16),
        Register('w13w12', 4, 0x18),
        Register('w12', 2, 0x18),
        Register('w12byte', 1, 0x18),
        Register('w13', 2, 0x1a),
        Register('w13byte', 1, 0x1a),
        Register('w15w14', 4, 0x1c),
        Register('w14', 2, 0x1c),
        Register('w14byte', 1, 0x1c),
        Register('w15', 2, 0x1e),
        Register('w15byte', 1, 0x1e),
        Register('splim', 2, 0x20),
        Register('acca', 6, 0x22),
        Register('accal', 2, 0x22),
        Register('accah', 2, 0x24),
        Register('accau', 2, 0x26),
        Register('accb', 6, 0x28),
        Register('accbl', 2, 0x28),
        Register('accbh', 2, 0x2a),
        Register('accbu', 2, 0x2c),
        Register('pc', 3, 0x2e, alias_names=('ip',)),
        Register('tblpag', 1, 0x31),
        Register('psvpag', 1, 0x33),
        Register('rcount', 2, 0x36),
        Register('dcount', 2, 0x38),
        Register('dostart', 3, 0x3a),
        Register('doend', 3, 0x3c),
        Register('corcon', 2, 0x44),
        Register('modcon', 2, 0x46),
        Register('xmodsrt', 2, 0x48),
        Register('xmodend', 2, 0x4a),
        Register('ymodsrt', 2, 0x4c),
        Register('ymodend', 2, 0x4e),
        Register('xbrev', 2, 0x50),
        Register('disicnt', 2, 0x52),
        Register('shadow_w0', 2, 0x0),
        Register('shadow_w1', 2, 0x2),
        Register('shadow_w2', 2, 0x4),
        Register('shadow_w3', 2, 0x6),
        Register('srl', 1, 0x400),
        Register('srh', 1, 0x401),
        Register('srh_oa', 1, 0x600),
        Register('srh_ob', 1, 0x601),
        Register('srh_sa', 1, 0x602),
        Register('srh_sb', 1, 0x603),
        Register('srh_oab', 1, 0x604),
        Register('srh_sab', 1, 0x605),
        Register('srh_da', 1, 0x606),
        Register('srh_dc', 1, 0x607),
        Register('srl_ipl2', 1, 0x608),
        Register('srl_ipl1', 1, 0x609),
        Register('srl_ipl0', 1, 0x60a),
        Register('srl_ra', 1, 0x60b),
        Register('srl_n', 1, 0x60c),
        Register('srl_ov', 1, 0x60d),
        Register('srl_z', 1, 0x60e),
        Register('srl_c', 1, 0x60f),
        Register('disi', 1, 0x610),
        Register('shadow_srh_dc', 1, 0x611),
        Register('shadow_srl_n', 1, 0x612),
        Register('shadow_srl_ov', 1, 0x613),
        Register('shadow_srl_z', 1, 0x614),
        Register('shadow_srl_c', 1, 0x615),
        Register('dostart_shadow', 3, 0x800),
        Register('doend_shadow', 3, 0x803),
        Register('wdtcount', 2, 0xa00),
        Register('wdtprescalara', 2, 0xa02),
        Register('wdtprescalarb', 2, 0xa04),
        Register('corcon_var', 1, 0xc00),
        Register('corcon_ipl3', 1, 0xc01),
        Register('corcon_psv', 1, 0xc02),
        Register('corcon_sfa', 1, 0xc03),
        Register('dcount_shadow', 2, 0x1000),
        Register('skipnextflag', 1, 0x1200),
        Register('contextreg', 4, 0x1400)
    ]

register_arch(['dspic30f:le:24:default'], 24, Endness.LE, ArchPcode_dsPIC30F_LE_24_default)
