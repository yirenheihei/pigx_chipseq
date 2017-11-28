#----------------------------------------------------------------------------- #
rule link_annotation:
        input:
            annotation = ANNOTATION['gtf'],
        output:
            outfile = os.path.join(PATH_ANNOTATION, 'GTF_Link.gtf')
        params:
            threads   = 1,
            mem       = '16G',
        message:"""
                Running: link_annotation:
                    output: {output.outfile}
            """
        shell:"""
            ln -s {input.annotation} {output.outfile}
        """


#----------------------------------------------------------------------------- #
rule prepare_annotation:
        input:
            gtf_path = rules.link_annotation.output.outfile
        output:
            outfile = os.path.join(PATH_ANNOTATION, 'Processed_Annotation.rds')
        params:
            threads   = 1,
            mem       = '16G',
            scriptdir = SCRIPT_PATH
        log:
            log = os.path.join(PATH_LOG, 'prepare_annotation.log')
        message:"""
                Running: prepare_annotation:
                    output: {output.outfile}
            """
        script:
            os.path.join(SCRIPT_PATH, 'Prepare_Annotation.R')