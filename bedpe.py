#!/usr/bin/env python

tab  = '\t'
endl = '\n'

from my_utils import *

class Bedpe:
    def __init__(self, chrm1, start1, end1, chrm2, start2, end2):
        self.chrm1 = chrm1
        self.start1 = int(start1)
        self.end1 = int(end1) 
        self.mean1 = (self.start1 + self.end1)/2
        self.chrm2 = chrm2
        self.start2 = int(start2)
        self.end2 = int(end2) 
        self.mean2 = (self.start2 + self.end2)/2

    def output_core(self):

        outstring = '%s\t%d\t%d\t%s\t%d\t%d' % (self.chrm1, self.start1, self.end1, self.chrm2, self.start2, self.end2)

        return outstring

class PairedBkCand:
    def __init__(self, attr_list):             
        self.chrm1, self.start1, self.end1, self.chrm2, self.start2, self.end2, self.svtype, self.svlength, self.endtype1, self.endtype2, self.n_supp = attr_list[0:11]
        self.start1 = int(self.start1)
        self.end1 = int(self.end1)
        self.start2 = int(self.start2)
        self.end2 = int(self.end2)
        self.n_supp = int(self.n_supp)

    def mean1(self):
        return int((self.start1 + self.end1)/2)

    def mean2(self):
        return int((self.start2 + self.end2)/2)

    def output(self):
        outstring = '%s\t%d\t%d\t%s\t%d\t%d\t%s\t%s\t%s\t%s\t%d' % (self.chrm1, self.start1, self.end1, self.chrm2, self.start2, self.end2, self.svtype, self.svlength, self.endtype1, self.endtype2, self.n_supp) 
        return outstring

    def tid1(self, chrname2tid):
        return chrname2tid[self.chrm1]
    def tid2(self, chrname2tid):
        return chrname2tid[self.chrm2] 

    def format_self(self, chrname2tid):
        if chrname2tid[self.chrm1] * FIX_LENGTH + self.start1 > chrname2tid[self.chrm2] * FIX_LENGTH + self.start2: 
            tmp1, tmp2, tmp3, tmp4 = self.chrm1, self.start1, self.end1, self.endtype1
            self.chrm1, self.start1, self.end1, self.endtype1 = self.chrm2, self.start2, self.end2, self.endtype2
            self.chrm2, self.start2, self.end2, self.endtype2 = tmp1, tmp2, tmp3, tmp4


class QuantifiedBKCand:

    def __init__(self, attr_list):

        self.chrm1, self.start1, self.end1, self.chrm2, self.start2, self.end2, self.svtype, self.svlength, self.num_fragment_support, self.endtype1, self.endtype2, self.score, self.logp_nosv_one_mol, self.logp_nosv_two_mol, self.logp_sv_one_mol, self.logp_sv_two_mol, self.type_score, self.endtype1_logp, self.endtype2_logp, self.start1_logp, self.end1_logp, self.start2_logp, self.end2_logp, self.support_frm_ids1, self.support_frm_ids2, self.support_barcodes, self.tid1, self.tid2 = attr_list[0:28]

        self.tid1 = int(self.tid1)
        self.start1 = int(self.start1)
        self.end1 = int(self.end1)

        self.tid2 = int(self.tid2)
        self.start2 = int(self.start2)
        self.end2 = int(self.end2)
   
        self.score = float(self.score)
        self.logp_nosv_one_mol = float(self.logp_nosv_one_mol)
        self.logp_nosv_two_mol = float(self.logp_nosv_two_mol)
        self.logp_sv_one_mol = float(self.logp_sv_one_mol)
        self.logp_sv_two_mol = float(self.logp_sv_two_mol)
        self.type_score = float(self.type_score)
        self.endtype1_logp = float(self.endtype1_logp)
        self.endtype2_logp = float(self.endtype2_logp)
        self.start1_logp = float(self.start1_logp)
        self.end1_logp = float(self.end1_logp)
        self.start2_logp = float(self.start2_logp)
        self.end2_logp = float(self.end2_logp)
        self.num_fragment_support = int(self.num_fragment_support)
        self.svlength = str(self.svlength)


    def attr_list(self):
        return [self.chrm1, self.start1, self.end1, self.chrm2, self.start2, self.end2, self.svtype, self.svlength, self.num_fragment_support, self.endtype1, self.endtype2, self.score, self.logp_nosv_one_mol, self.logp_nosv_two_mol, self.logp_sv_one_mol, self.logp_sv_two_mol, self.type_score, self.endtype1_logp, self.endtype2_logp, self.start1_logp, self.end1_logp, self.start2_logp, self.end2_logp, self.support_frm_ids1, self.support_frm_ids2, self.support_barcodes, self.tid1, self.tid2] 

    def output_svcall(self):

        outstring = '%s\t%d\t%d\t%s\t%d\t%d\t%s\t%s' % (self.chrm1, self.start1, self.end1, self.chrm2, self.start2, self.end2, self.svtype, self.svlength)
        return outstring

    def output(self):

        outstring = '%s\t%d\t%d\t%s\t%d\t%d\t%s\t%s\t%d\t%s\t%s\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%s\t%s\t%s\t%d\t%d' % (self.chrm1, self.start1, self.end1, self.chrm2, self.start2, self.end2, self.svtype, self.svlength, self.num_fragment_support, self.endtype1, self.endtype2, self.score, self.logp_nosv_one_mol, self.logp_nosv_two_mol, self.logp_sv_one_mol, self.logp_sv_two_mol, self.type_score, self.endtype1_logp, self.endtype2_logp, self.start1_logp, self.end1_logp, self.start2_logp, self.end2_logp, self.support_frm_ids1, self.support_frm_ids2, self.support_barcodes, self.tid1, self.tid2)

        return outstring

    def output_core(self):
        outstring = '%s\t%d\t%d\t%s\t%d\t%d\t%s\t%s\t%d\t%s\t%s\t%.2f\t%.2f\t%s' % (self.chrm1, self.start1, self.end1, self.chrm2, self.start2, self.end2, self.svtype, self.svlength, self.num_fragment_support, self.endtype1, self.endtype2, self.score, self.logp_nosv_one_mol, self.support_barcodes.rstrip(','))
        return outstring

    def frm_id_list1(self):
        frm_id_list1 = self.support_frm_ids1.strip(',').split(',')
        for i in range(0, len(frm_id_list1)):
            frm_id_list1[i] = int(frm_id_list1[i])
        return frm_id_list1

    def frm_id_list2(self):
        frm_id_list2 = self.support_frm_ids2.strip(',').split(',')
        for i in range(0, len(frm_id_list2)):
            frm_id_list2[i] = int(frm_id_list2[i])
        return frm_id_list2

    def frm_id_set1(self):
        return set(self.frm_id_list1())

    def frm_id_set2(self):
        return set(self.frm_id_list2())

    def all_frm_id_set(self):
        return set(self.frm_id_list1()).union(set(self.frm_id_list2()))


class RefinedQuantBKCand(QuantifiedBKCand):

    def __init__(self, attr_list):
        QuantifiedBKCand.__init__(self, attr_list[0:28])
        self.refine_score, self.n_pe_support, self.n_sr_support, self.n_support_reads, self.refined_bk1, self.refined_bk2 = attr_list[28:34]
        self.refine_score = float(self.refine_score)
        self.n_pe_support = int(self.n_pe_support)
        self.n_sr_support = int(self.n_sr_support)
        self.n_support_reads = int(self.n_support_reads)
        self.refined_bk1 = int(self.refined_bk1)
        self.refined_bk2 = int(self.refined_bk2)

    def output(self):

        outstring = QuantifiedBKCand.output(self) + '\t%.2f\t%d\t%d\t%d\t%d\t%d'  % (self.refine_score, self.n_pe_support, self.n_sr_support, self.n_support_reads, self.refined_bk1, self.refined_bk2)  

        return outstring

def read_paired_bk_cand_file(paired_bk_cand_file):

    paired_bk_cand_list = list()
    paired_bk_cand_fp = open(paired_bk_cand_file, 'r')
    while 1:
        line = paired_bk_cand_fp.readline()
        if not line: break
        line = line.strip().split(tab)
        paired_bk_cand = PairedBkCand(line)
        paired_bk_cand_list.append(paired_bk_cand)

    paired_bk_cand_fp.close()
    return paired_bk_cand_list

##### BedpeBkPair #####
class BedpeBkPair(Bedpe):

    def __init__(self, line, chrname2tid):

        Bedpe.__init__(self, line[0], line[1], line[2], line[3], line[4], line[5])

        self.join_type = line[6] 
        if len(line) > 7: 
            self.score = int(line[7])
        else:
            self.score = None

        self.tid1 = chrname2tid[chrm1]
        self.tid2 = chrname2tid[chrm2]

    def output_svcall(self):
        outstring = '%s\t%d\t%d\t%s\t%d\t%d\t%s' % (self.chrm1, self.start1, self.end1, self.chrm2, self.start2, self.end2, self.join_type)
        return outstring

def read_BedpeBkPair_file(in_file, chrname2tid):
    in_fp = open(in_file, 'r')
    line = list(in_fp)
    bedpe_list = list()
    in_fp.close()

    for line in lines:
        if line[0] == '#': continue
        line = line.strip().split(tab)
        bedpe = BedpeBkPair(line, chrname2tid)
        bedpe_list.append(bedpe)

    return bedpe_list

##### BedpeBkPair #####

class BedpeSVCall(Bedpe):
    def __init__(self, chrm1, start1, end1, chrm2, start2, end2, svtype, chrname2tid, info = None):
        Bedpe.__init__(self, chrm1, start1, end1, chrm2, start2, end2)

        if svtype:
            self.svtype = svtype
        else:
            self.svtype = 'UNK'
        
        self.info = info
        self.tid1 = chrname2tid[chrm1]
        self.tid2 = chrname2tid[chrm2]
        self.key1 = self.tid1 * FIX_LENGTH + self.mean1
        self.key2 = self.tid2 * FIX_LENGTH + self.mean2

    def output_svcall(self):
        outstring = '%s\t%d\t%d\t%s\t%d\t%d\t%s' % (self.chrm1, self.start1, self.end1, self.chrm2, self.start2, self.end2, self.svtype)
        return outstring
    
    def output_bkpos(self):
        outstring = '%s:%d, %s:%d, %s' % (self.chrm1, self.mean1, self.chrm2, self.mean2, self.svtype)
        return outstring

    def output_bk1pos(self):
        outstring = '%s:%d %s' % (self.chrm1, self.mean1, self.svtype)
        return outstring

    def output_bk2pos(self):
        outstring = '%s:%d %s' % (self.chrm2, self.mean2, self.svtype)
        return outstring

def read_bedpe_file(in_bedpe_file):

    in_bedpe_fp = open(in_bedpe_file, 'r')
    lines = list(in_bedpe_fp)
    in_bedpe_fp.close()

    bedpe_list = list()
    for line in lines:
        line = line.strip().split(tab)
        bedpe = Bedpe(line[0], line[1], line[2], line[3], line[4], line[5])
        bedpe_list.append(bedpe)

    return bedpe_list

def read_svcall_bedpe_file(in_bedpe_file, chrname2tid):

    in_bedpe_fp = open(in_bedpe_file, 'r')
    lines       = list(in_bedpe_fp)
    in_bedpe_fp.close()

    bedpe_list = list()
    for line in lines:
        if line[0] == '#':
            continue
        line = line.strip().split(tab)
        if len(line) >= 7:
            bedpe = BedpeSVCall(line[0], line[1], line[2], line[3], line[4], line[5], line[6], chrname2tid)
        else:
            bedpe = BedpeSVCall(line[0], line[1], line[2], line[3], line[4], line[5], 'UNK', chrname2tid)
        bedpe_list.append(bedpe)

    return bedpe_list

def format_svcall_bedpe(bedpe_list):

    formatted_bedpe_list = list()

    for bedpe in bedpe_list:
        if bedpe.key1 > bedpe.key2:
            tmp1, tmp2, tmp3, tmp4, tmp5 = bedpe.chrm1, bedpe.start1, bedpe.end1, bedpe.tid1, bedpe.key1
            bedpe.chrm1, bedpe.start1, bedpe.end1, bedpe.tid1, bedpe.key1 = bedpe.chrm2, bedpe.start2, bedpe.end2, bedpe.tid2, bedpe.key2
            bedpe.chrm2, bedpe.start2, bedpe.end2, bedpe.tid2, bedpe.key2 = tmp1, tmp2, tmp3, tmp4, tmp5

        formatted_bedpe_list.append(bedpe)

    return formatted_bedpe_list
