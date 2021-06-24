import pytest
import tema1

def test_hayval():
    elmes = 'Enero'
    hayvalores = 100
    assert tema1.hayval(elmes) == tema1.tipodato(elmes)

def test_tipodato():
    elmes = 'Enero'
    assert tema1.tipodato(elmes) == tema1.calculos(elmes)

def test_calculos():
    elmes = 'Enero'
    assert tema1.calculos(elmes) == tema1.informe()

def test_informe():
    maxgasto = 'Abril'
    maxahorro = 'Enero'
    mediagasto = -24732
    gastototal = -296791
    ingresototal = 280961
    assert maxgasto == tema1.informe.maxgasto
    assert maxahorro == tema1.informe.maxahorro
    assert mediagasto == tema1.informe.mediagasto
    assert gastototal == tema1.informe.gastototal
    assert ingresototal == tema1.informe.ingresototal

