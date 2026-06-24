// sd-def-schema.ts (generated)

export interface Asset {
  id: string;
  name: string;
  type: "host" | "service" | "application" | "user" | "network";
  tags?: string[];
  criticality?: "low" | "medium" | "high" | "critical";
}

export interface ControlFrameworkRef {
  framework: "NIST-CSF";
  function: "Identify" | "Protect" | "Detect" | "Respond" | "Recover";
  category: string;
  subcategory: string;
}

export interface Control {
  id: string;
  name: string;
  frameworkRef: ControlFrameworkRef;
  owner?: string;
}

export interface SignalBase {
  id: string;
  source: string;
  timestamp: string; // ISO
  assetId?: string;
  controlId?: string;
  severity?: "info" | "low" | "medium" | "high" | "critical";
  details?: Record<string, unknown>;
}

export type DegradationEventType =
  | "misconfiguration"
  | "process_drift"
  | "visibility_loss"
  | "control_failure"
  | "surface_expansion";

export interface DegradationEvent {
  id: string;
  type: DegradationEventType;
  assetId: string;
  controlId?: string;
  timestamp: string;
  signalIds: string[];
  impactSurfaceId?: string;
}

export interface ImpactSurface {
  id: string;
  assetIds: string[];
  userSegments?: string[];
  dataClasses?: string[];
}

export interface ScoreBase {
  id: string;
  eventId: string;
  value: number;
  scale: number;
  dimension?: string;
}

export interface ControlWeakeningScore extends ScoreBase {
  dimension: "control_weakening";
}

export interface ExposureAmplificationScore extends ScoreBase {
  dimension: "exposure_amplification";
}

export interface DetectionBlindnessScore extends ScoreBase {
  dimension: "detection_blindness";
}

export interface ProcessErosionScore extends ScoreBase {
  dimension: "process_erosion";
}

export type AnyScore =
  | ControlWeakeningScore
  | ExposureAmplificationScore
  | DetectionBlindnessScore
  | ProcessErosionScore;

export type SDIScopeType = "asset" | "control" | "global";

export interface SDIScope {
  type: SDIScopeType;
  assetId?: string;
  controlId?: string;
}

export interface SecurityDegradationIndex {
  id: string;
  scope: SDIScope;
  value: number;
  scale: number;
  components?: {
    controlWeakening?: number;
    exposureAmplification?: number;
    detectionBlindness?: number;
    processErosion?: number;
  };
}

export type RemediationType =
  | "immediate_fix"
  | "structural_remediation"
  | "control_hardening"
  | "visibility_restoration";

export type RemediationPriority = "p0" | "p1" | "p2" | "p3";

export interface RemediationAction {
  id: string;
  type: RemediationType;
  priority: RemediationPriority;
  title: string;
  description?: string;
  relatedEventIds?: string[];
  owner?: string;
}
