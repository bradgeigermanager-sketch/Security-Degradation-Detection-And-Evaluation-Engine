# sd_def_schema.py (generated)

from typing import List, Optional, Literal, Dict, Any
from pydantic import BaseModel


class Asset(BaseModel):
    id: str
    name: str
    type: Literal["host", "service", "application", "user", "network"]
    tags: Optional[List[str]] = None
    criticality: Optional[Literal["low", "medium", "high", "critical"]] = None


class ControlFrameworkRef(BaseModel):
    framework: Literal["NIST-CSF"]
    function: Literal["Identify", "Protect", "Detect", "Respond", "Recover"]
    category: str
    subcategory: str


class Control(BaseModel):
    id: str
    name: str
    frameworkRef: ControlFrameworkRef
    owner: Optional[str] = None


class SignalBase(BaseModel):
    id: str
    source: str
    timestamp: str  # ISO 8601
    assetId: Optional[str] = None
    controlId: Optional[str] = None
    severity: Optional[Literal["info", "low", "medium", "high", "critical"]] = None
    details: Optional[Dict[str, Any]] = None


DegradationEventType = Literal[
    "misconfiguration",
    "process_drift",
    "visibility_loss",
    "control_failure",
    "surface_expansion",
]


class DegradationEvent(BaseModel):
    id: str
    type: DegradationEventType
    assetId: str
    controlId: Optional[str] = None
    timestamp: str
    signalIds: List[str]
    impactSurfaceId: Optional[str] = None


class ImpactSurface(BaseModel):
    id: str
    assetIds: List[str]
    userSegments: Optional[List[str]] = None
    dataClasses: Optional[List[str]] = None


class ScoreBase(BaseModel):
    id: str
    eventId: str
    value: float
    scale: float
    dimension: Optional[str] = None


class ControlWeakeningScore(ScoreBase):
    dimension: Literal["control_weakening"] = "control_weakening"


class ExposureAmplificationScore(ScoreBase):
    dimension: Literal["exposure_amplification"] = "exposure_amplification"


class DetectionBlindnessScore(ScoreBase):
    dimension: Literal["detection_blindness"] = "detection_blindness"


class ProcessErosionScore(ScoreBase):
    dimension: Literal["process_erosion"] = "process_erosion"


SDIScopeType = Literal["asset", "control", "global"]


class SDIScope(BaseModel):
    type: SDIScopeType
    assetId: Optional[str] = None
    controlId: Optional[str] = None


class SecurityDegradationIndex(BaseModel):
    id: str
    scope: SDIScope
    value: float
    scale: float
    components: Optional[Dict[str, float]] = None


RemediationType = Literal[
    "immediate_fix",
    "structural_remediation",
    "control_hardening",
    "visibility_restoration",
]

RemediationPriority = Literal["p0", "p1", "p2", "p3"]


class RemediationAction(BaseModel):
    id: str
    type: RemediationType
    priority: RemediationPriority
    title: str
    description: Optional[str] = None
    relatedEventIds: Optional[List[str]] = None
    owner: Optional[str] = None
